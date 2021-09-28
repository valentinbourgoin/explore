from stravalib.client import Client
from allauth.socialaccount.models import SocialToken, SocialApp
from django.utils import timezone
from django.utils.timezone import make_aware

from explore import settings
from datetime import datetime

class StravaClientMixin(object):
  provider_name = "strava"

  def get_client(self, user):
    try:
      token = SocialToken.objects.get(
        account__user=user, 
        account__provider=self.provider_name)
      client = Client(access_token=token.token)
    except SocialToken.DoesNotExist:
      return None

    if (token.expires_at <= timezone.now()):
      client = self.refresh_token(token, client)
      
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

    # Refresh stored django allauth token
    token.access_token = refresh['access_token']
    token.token_secret = refresh['refresh_token']
    token.expires_at = make_aware(datetime.fromtimestamp(refresh['expires_at']))
    token.save()

    return Client(access_token=token.access_token)