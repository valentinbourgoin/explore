from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from map.models import Tile, Grid
from api.serializers.activities import SimpleActivitySerializer

class TileSerializer(GeoFeatureModelSerializer):
    activity_related = SimpleActivitySerializer(many=False, read_only=True)

    class Meta:
        model = Tile
        fields = ['status', 'activity_related']
        geo_field = 'points'

class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ['id', 'name', 'status', 'center_point']
