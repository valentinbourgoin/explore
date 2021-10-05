import json
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse

from core.models import User
from api.views.users import UserViewSet

class UserTest(APITestCase):
    def setUp(self): 
        self.user = User.objects.create_user(
            pk=1, 
            username='julian', 
            email='julian@quikstep.com', 
            password='worldchampion2021'
        )
        self.token = Token.objects.create(user=self.user)

    def test_me(self):
        '''
        Test /api/users/me path
        '''
        url = reverse('user-me')
        client = APIClient()

        # Check if /api/users/me is unauthorized when user is anonymous 
        response_anonymous = client.get(url)
        self.assertEqual(response_anonymous.status_code, status.HTTP_401_UNAUTHORIZED)

        # Check if /api/users/me is correct when Julian is logged in
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response_auth = client.get(url)
        self.assertEqual(response_auth.status_code, status.HTTP_200_OK)
        self.assertEqual(response_auth.data, {'id': 1, 'username': 'julian', 'avatar': None})

    def test_pull(self):
        '''
        Test /api/users/[id]/pull path
        '''
        url = reverse('user-pull', kwargs={'pk': 1})
        client = APIClient()

        # Check if anonymous call to /api/users/1/pull returns an error
        response_anonymous = client.get(url)
        self.assertEqual(response_anonymous.status_code, status.HTTP_401_UNAUTHORIZED)

        # Check if /api/users/1/pull returns a well formatted object
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response_auth = client.get(url)
        self.assertEqual(response_auth.status_code, status.HTTP_200_OK)
        self.assertEqual(response_auth.data['success'], True)

        # Check if /api/users/123/pull returns a 404 error
        url_error = reverse('user-pull', kwargs={'pk': 123})
        response_error = client.get(url_error)
        self.assertEqual(response_error.status_code, status.HTTP_403_FORBIDDEN)

