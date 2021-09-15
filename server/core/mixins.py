from stravalib.client import Client
from social_django.utils import load_strategy
import time

class StravaClientMixin(object):
  def get_strava_client(self, user):
    strava = user.social_auth.get(provider="strava")
    if (strava.extra_data['auth_time'] + strava.extra_data['expires']) <= int(time.time()):
      strategy = load_strategy()
      strava.refresh_token(strategy)
    client = Client(access_token=strava.access_token)
    return client
