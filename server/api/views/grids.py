from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from api.serializers.grids import GridSerializer, TileSerializer
from map.models import Grid

class GridViewSet(viewsets.ViewSet):
    queryset = Grid.objects.all()
    serializer_class = GridSerializer

    def list(self, request):
        serializer = GridSerializer(Grid.objects.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        grid = get_object_or_404(Grid, pk=pk)
        serializer = GridSerializer(grid)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True)
    def tiles(self, request, pk=None):
        grid = get_object_or_404(Grid, pk=pk)
        serializer = TileSerializer(grid.tiles.all(), many=True, context={'request': request})
        return Response(serializer.data)
    