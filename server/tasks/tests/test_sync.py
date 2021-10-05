from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialToken, SocialApp, SocialAccount

from core.models import User
from tasks.sync_activities import get_activities_by_user
from explore import settings

class SyncTest(TestCase):
    '''
    All tests related to sync activities task
    '''
    def setUp(self): 
        self.user_no_connection = User.objects.create_user(
            pk=1, 
            username='julian', 
            email='julian@quikstep.com', 
            password='worldchampion2021'
        )

        self.user_strava = User.objects.create_user(
            pk=2, 
            username='julian_rainbow', 
            email='julian+rainbow@quikstep.com', 
            password='worldchampion2021'
        )
        self.social_app = SocialApp.objects.create(
            provider='strava',
            name='Strava',
            client_id="xxxx",
            secret="xxxx"
        )
        self.social_app.sites.add(Site.objects.get(pk=settings.SITE_ID))
        self.social_account = SocialAccount.objects.create(
            user=self.user_strava,
            provider='strava',
            uid=11111
        )
        self.social_token_valid = SocialToken.objects.create(
            app=self.social_app,
            account=self.social_account,
            token='azerty',
            token_secret='qsdfg',
            expires_at=timezone.now() + timedelta(hours=2)
        )

    def test_get_activities_by_user(self):
        # Check if method returns none if user has no social connection
        result_none = get_activities_by_user(self.user_no_connection.id)
        self.assertEqual(result_none, None)

        # Check if method returns an empty object if user has valid token
        result_strava = get_activities_by_user(self.user_strava.id)
        self.assertEqual(result_strava, {})



