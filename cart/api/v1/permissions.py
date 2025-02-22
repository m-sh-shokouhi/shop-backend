from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission

class OrderPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user