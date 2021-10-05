from datetime import datetime
from stravalib.client import Client as Stravalib
from allauth.socialaccount.models import SocialApp
from django.utils import timezone
from django.utils.timezone import make_aware

from explore import settings
from core.backend.abstract import AbstractClient

class StravaClient(AbstractClient):
  '''
  Strava client mixin class
  Use stravalib methods to call Strava API
  '''
  provider_name = "strava"

  def get_client(self):
    token = self.get_social_token()
    if (token is not None):
      self.client = Stravalib(access_token=token.token)      

      if (token.expires_at <= timezone.now()):
        self.refresh_token(token)
      
      return self.client
    return None

  def refresh_token(self, token): 
    # Refresh stravalib client
    try:
      social_app = SocialApp.objects.get(
        provider=self.provider_name,
        sites__id=settings.SITE_ID
      )
    except SocialApp.DoesNotExist:
      return None

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