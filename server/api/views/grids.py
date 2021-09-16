from rest_framework import generics
from api.serializers import TileSerializer

class ListTiles(generics.ListAPIView):
    serializer_class = TileSerializer

    def get_queryset(self):
        grid = self.kwargs['grid']
        return Tile.objects.filter(grid__id=grid)

