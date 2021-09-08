from stravalib.client import Client

class StravaClientMixin(object):
  def get_strava_client(self, user):
    strava = user.social_auth.get()
    return Client(access_token=strava.access_token)
