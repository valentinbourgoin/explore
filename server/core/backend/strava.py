from stravalib.client import Client as StravaClient
from allauth.socialaccount.models import SocialToken, SocialApp
from django.utils import timezone
from django.utils.timezone import make_aware

from explore import settings
from datetime import datetime

'''
Strava client mixin class
Use stravalib methods to call Strava API
'''
class StravaClient():
  provider_name = "strava"

  def get_client(self, user):
    token = self.get_social_token(user)
    client = StravaClient(access_token=token.token)      

    if (token.expires_at <= timezone.now()):
      return self.refresh_token(token, client)
      
    return client

  def refresh_token(self, token, client): 
    # Refresh stravalib client
    social_app = SocialApp.objects.get(
      provider=self.provider_name,
      sites__id=settings.SITE_ID
    )
    refresh = client.refresh_access_token(
      social_app.client_id,
      social_app.secret,
      token.token_secret
    )

    self.update_refresh_token(
      refresh['access_token'],
      refresh['refresh_token'],
      make_aware(datetime.fromtimestamp(refresh['expires_at']))
    )
    
    return StravaClient(access_token=token.access_token)