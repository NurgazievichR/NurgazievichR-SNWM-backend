from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsNotAuthenticated(BasePermission):
    message = 'Вы уже аутентифицированы'

    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated):
            raise PermissionDenied(self.message)
        return True 