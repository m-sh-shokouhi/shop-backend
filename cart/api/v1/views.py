from rest_framework import viewsets
from ...models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from .permissions import OrderPermission

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [OrderPermission]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [OrderPermission]