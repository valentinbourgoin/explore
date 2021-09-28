from django.urls import path, re_path
from rest_framework import routers

from .views.users import UserViewSet
from .views.grids import GridViewSet
from .views.auth import StravaLogin
from .views.tasks import TasksView

router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'grids', GridViewSet, basename='grid')

urlpatterns = [
    path('rest-auth/strava/', StravaLogin.as_view(), name='strava_login'),
    path("tasks/<task_id>/", TasksView.as_view(), name="get_task_status"),
]

urlpatterns += router.urls