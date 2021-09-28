from rest_framework import permissions

class IsAdminOrIsOwner(permissions.BasePermission):
    message = 'This action is not allowed for other users'

    def has_permission(self, request, view):
        if (request.user.is_authenticated):
            if (request.user.is_superuser):
                return True
            pk = request.parser_context['kwargs'].get('pk')
            if (pk):
                return int(pk) == request.user.id
        return False
