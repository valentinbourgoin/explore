from django.urls import path, re_path
from rest_framework import routers

from .views.users import UserViewSet
from .views.grids import ListTiles
from .views.auth import StravaLogin

router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    #path('users/', UserViewSet.as_view({'get': 'list'}), name='api_users'),
#    path('users/me/', UserViewSet.as_view({'get': 'me'}), name='api_users_me'),

    re_path('^grid/(?P<grid>.+)/tiles$', ListTiles.as_view(), name='api_tiles'),

    path('rest-auth/strava/', StravaLogin.as_view(), name='strava_login')
]

urlpatterns += router.urls