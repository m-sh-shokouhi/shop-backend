from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission

class ReadOnlyForUsers(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff