from requests.exceptions import HTTPError
from stravalib.client import Client 
from celery.utils.log import get_task_logger

import arrow

from core.models import Activity, User
from core.mixins import StravaClientMixin
from tasks.process_activities import process_activity
from explore.celery import app

logger = get_task_logger(__name__)

@app.task(bind=True)
def get_activities_by_user(self, user_id, days=None):
    logger.info(u"Getting order for user %d" % user_id)
    user = User.objects.get(id=user_id)
    result = {}

    #todo Refacto : get all clients
    client = StravaClientMixin().get_client(user)
    if (not client):
        logger.info(u'%s has no social token', user)
        return None

    # @todo replace days by last pull at
    if (days): 
        end = arrow.utcnow()
        start = end.shift(days=(0-days))
        activity_iter = client.get_activities(
            before=end.datetime,
            after=start.datetime
        )
    else:
        activity_iter = client.get_activities()

    try:
        result['activities_nb'] = sum(1 for _ in activity_iter)
        nb_of_activities_processed = 0
        result['activities_created'] = []
        result['subtasks'] = []
        logger.info(u'%d activities to get' % result['activities_nb'])
        for activity in activity_iter:
            act, created = Activity.objects.get_or_create(
                external_id=activity.id,
                user=user
            )
            act.update_from_strava(activity)
            if (not act.polylines):
                task = process_activity.delay(activity_id=act.id)
                result['subtasks'].append(task.id)
            
            if (created):
                result['activities_created'].append(act.id)
                logger.info(u'New activity created: %s' % act.name)
            else: 
                logger.info(u'Activity updated: %s' % act.name)

            nb_of_activities_processed += 1 
            self.update_state(
                state='PROGRESS', 
                meta={
                    'current': nb_of_activities_processed, 
                    'total': result['activities_nb']
                }
            )

    except HTTPError as e:
        # todo : reach limit
        # social.get().delete()
        logger.error(e)

    return result

# @app.task 
# def get_activity_details(activity_id):
#     logger.info(u"Getting details for activity %d" % activity_id)
#     activity = Activity.objects.get(id=activity_id)
#     client = StravaClientMixin().get_client(activity.user)
#     act = client.get_activity(activity.external_id)
#     activity.update_encoded_polyline(act.map.polyline)
#     process_activity_tails.delay(activity_id=activity_id)


@app.task(bind=True)
def retrieve_activities(days=None):
    users = User.objects.all().values_list('id', flat=True)
    logger.info(u"Activity pull order for %d users" % len(users))

    for user in users: 
        get_activities_by_user.delay(user_id=user, days=days)
        logger.info(u"Getting activities for user %d" % user)
