from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from ...models import Cart

class CartViewSetPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user
    

class CartItemPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            cart = Cart.objects.get(pk=request.data['cart'])
            if request.user.is_staff:
                return True
        except Cart.DoesNotExist:
            return False
        return cart.user == request.user
    
    def has_permission(self, request, view):
        
        try:
            cart = Cart.objects.get(pk=request.data['cart'])
            if request.user.is_staff:
                return True
        except Cart.DoesNotExist:
            return False
        return cart.user == request.user