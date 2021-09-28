from django.urls import path

from . import views
from map.models import Tile

urlpatterns = [
    path('', views.index, name='index'),
    path('grid/<int:grid_id>', views.grid_details, name='grid_details'),
]