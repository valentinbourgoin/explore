from requests.exceptions import HTTPError
from stravalib.client import Client 

import arrow

from explore.celery import app

from .models import Activity, User
from core.mixins import StravaClientMixin
from map.tasks import process_activity_tails

@app.task
def get_strava_activities_by_user(user_id, days=None):
    print(u"Getting order for user %d" % user_id)
    user = User.objects.get(id=user_id)
    social = user.social_auth.filter(provider='strava')

    if (not social.exists()):
        return None
    
    client = StravaClientMixin().get_strava_client(user)

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
        for activity in activity_iter: 
            act, created = Activity.objects.get_or_create(
                external_id=activity.id,
                user=user
            )
            act.update_from_strava(activity)
            if (not act.polylines):
                get_strava_activity_details.delay(activity_id=act.id)

    except HTTPError as e:
        # social.get().delete()
        print(e)

@app.task 
def get_strava_activity_details(activity_id):
    print(u"Getting details for activity %d" % activity_id)
    activity = Activity.objects.get(id=activity_id)
    client = StravaClientMixin().get_strava_client(activity.user)
    act = client.get_activity(activity.external_id)
    activity.update_encoded_polyline(act.map.polyline)
    process_activity_tails.delay(activity_id=activity_id)


@app.task
def retrieve_activities(days=None):
    users = User.objects.filter(
        social_auth__provider='strava'
    ).values_list('id', flat=True)

    for user in users: 
        get_strava_activities_by_user.delay(user_id=user, days=days)
        print(u"Getting activities for user %d" % user)
