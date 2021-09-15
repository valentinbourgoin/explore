from django.shortcuts import render, get_object_or_404
from map.models import Grid

from core.mixins import StravaClientMixin

def index(request):
    return render(request, 'core/index.html')

def grid_details(request, grid_id):
    grid = get_object_or_404(Grid, id=grid_id)
    context = { 'grid': grid }
    return render(request, 'core/grid_details.html', context)