from allauth.socialaccount.providers.strava.views import StravaOauth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class StravaLogin(SocialLoginView):
    adapter_class = StravaOauth2Adapter
    callback_url = "http://localhost:8000" # @todo
    client_class = OAuth2Client
