from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer
from core.models import User

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def me(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    