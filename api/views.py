from core.models import User
from rest_framework import viewsets, generics

from .serializers import UserSerializer, TileSerializer
from map.models import Tile

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TileList(generics.ListAPIView):
    serializer_class = TileSerializer

    def get_queryset(self):
        grid = self.kwargs['grid']
        return Tile.objects.filter(grid__id=grid)