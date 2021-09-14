from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from core.models import User, Activity
from map.models import Tile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'avatar']

class SimpleActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = ['user', 'activity_type', 'start_date']

class TileSerializer(GeoFeatureModelSerializer):
    activity_related = SimpleActivitySerializer(many=False, read_only=True)

    class Meta:
        model = Tile
        fields = ['status', 'activity_related']
        geo_field = "points"
