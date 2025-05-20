from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from ...models import Cart

class CartViewSetPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user
    

class CartItemPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if obj.cart.user == request.user:
            return True
        return False
    
    def has_permission(self, request, view):
        return request.user.is_authenticated