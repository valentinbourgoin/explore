from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import action
from celery.result import AsyncResult

from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer
from api.permissions import IsAdminOrIsOwner
from core.models import User
from tasks.tasks.sync_activities import get_activities_by_user

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ permissions.IsAuthenticated ]
    
    @action(methods=['get'], detail=False)
    def me(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True, permission_classes=[IsAdminOrIsOwner])
    def pull(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        task = get_activities_by_user.delay(
            user_id=user.id, 
            days=3 # @todo : since last pull
        )
        return Response({
            "success": True, 
            "task_id": task.id
        })