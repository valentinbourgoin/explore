from rest_framework import serializers

from core.models import Activity
from api.serializers.users import UserSerializer

class SimpleActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = ['user', 'activity_type', 'distance', 'start_date']

