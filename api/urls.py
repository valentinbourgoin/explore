from django.urls import path, re_path, include
from rest_framework import routers

from .views import UserViewSet, TileList

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
# @todo add tiles in the router

urlpatterns = [
    path('', include(router.urls)),

    re_path('^grid/(?P<grid>.+)/tiles$', TileList.as_view(), name="api_tiles"),

    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]