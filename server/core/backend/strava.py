from stravalib.client import Client as Stravalib
from allauth.socialaccount.models import SocialToken, SocialApp
from django.utils import timezone
from django.utils.timezone import make_aware
from core.backend.abstract import AbstractClient

from explore import settings
from datetime import datetime

'''
Strava client mixin class
Use stravalib methods to call Strava API
'''
class StravaClient(AbstractClient):
  provider_name = "strava"

  def get_client(self):
    token = self.get_social_token()
    self.client = Stravalib(access_token=token.token)      

    if (token.expires_at <= timezone.now()):
      self.refresh_token(token)
      
    return self.client

  def refresh_token(self, token): 
    # Refresh stravalib client
    social_app = SocialApp.objects.get(
      provider=self.provider_name,
      sites__id=settings.SITE_ID
    )
    refresh = self.client.refresh_access_token(
      social_app.client_id,
      social_app.secret,
      token.token_secret
    )

    self.update_refresh_token(
      refresh['access_token'],
      refresh['refresh_token'],
      make_aware(datetime.fromtimestamp(refresh['expires_at']))
    )
    
    self.client = StravaClient(access_token=token.access_token)