from requests.exceptions import HTTPError
from stravalib.client import Client 

import arrow

from explore.celery import app

from .models import Activity, User
from core.mixins import StravaClientMixin
from map.tasks import process_activity_tails

@app.task(bind=True)
def get_activities_by_user(self, user_id, days=None):
    print(u"Getting order for user %d" % user_id)
    user = User.objects.get(id=user_id)

    #todo Refacto : get all clients
    client = StravaClientMixin().get_client(user)
    if (not client):
        print (u'%s has no social token', user)
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
        activity_nb = sum(1 for _ in activity_iter)
        activity_processed = 0
        print (u'%d activities to get' % activity_nb)
        for activity in activity_iter:
            act, created = Activity.objects.get_or_create(
                external_id=activity.id,
                user=user
            )
            act.update_from_strava(activity)
            if (not act.polylines):
                get_activity_details.delay(activity_id=act.id)
            
            activity_processed += 1 
            #@todo : set progress ? 
            self.update_state(
                state='PROGRESS', 
                meta={'current': activity_processed, 'total': activity_nb
            })

    except HTTPError as e:
        # todo : reach limit
        # social.get().delete()
        print(e)

@app.task 
def get_activity_details(activity_id):
    print(u"Getting details for activity %d" % activity_id)
    activity = Activity.objects.get(id=activity_id)
    client = StravaClientMixin().get_client(activity.user)
    act = client.get_activity(activity.external_id)
    activity.update_encoded_polyline(act.map.polyline)
    process_activity_tails.delay(activity_id=activity_id)


@app.task
def retrieve_activities(days=None):
    users = User.objects.all().values_list('id', flat=True)
    for user in users: 
        get_activities_by_user.delay(user_id=user, days=days)
        print(u"Getting activities for user %d" % user)
