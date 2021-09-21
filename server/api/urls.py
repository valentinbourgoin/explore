from django.urls import path, re_path
from rest_framework import routers

from .views.users import UserViewSet
from .views.grids import GridViewSet
from .views.auth import StravaLogin

router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'grids', GridViewSet, basename='grid')

urlpatterns = [
    path('rest-auth/strava/', StravaLogin.as_view(), name='strava_login')
]

urlpatterns += router.urls