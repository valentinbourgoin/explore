from requests.exceptions import HTTPError
from celery.utils.log import get_task_logger
from allauth.socialaccount.models import SocialApp

from core.models import Activity, User, UserSync
from core.backend.strava import StravaClient
from tasks.process_activities import process_activity
from explore.celery import app

logger = get_task_logger(__name__)

@app.task(bind=True)
def get_activities_by_user(self, user_id):
    logger.info(u"Getting order for user %d" % user_id)
    user = User.objects.get(id=user_id)
    result = {}

    #todo Refacto : get all clients
    client = StravaClient(user).client
    if (not client):
        logger.info(u'%s has no social token', user)
        return None

    # @todo helper 
    try:
        usersync = UserSync.objects.get(
            user=user, 
            app__provider="strava"
        )
    except UserSync.DoesNotExist:
        usersync = UserSync()
        usersync.last_updated_at = user.date_joined

    activity_iter = client.get_activities(
        after=usersync.last_updated_at
    )
    
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
            # @todo : remove method and use backend manager
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
    
    # @todo
    usersync.user = user
    usersync.app = SocialApp.objects.get(provider="strava")
    usersync.save()

    return result


@app.task(bind=True)
def retrieve_activities():
    users = User.objects.all().values_list('id', flat=True)
    logger.info(u"Activity pull order for %d users" % len(users))

    for user in users: 
        get_activities_by_user.delay(user_id=user)
        logger.info(u"Getting activities for user %d" % user)
