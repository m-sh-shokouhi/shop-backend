from rest_framework import viewsets
from ...models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from .permissions import OrderPermission
from rest_framework.response import Response
from rest_framework import status

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [OrderPermission]
    
    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == 'latest':
            user = request.user
            if user.is_authenticated:
                queryset = self.queryset.filter(user=user)
                if queryset.exists():
                    instance = queryset.latest("created_at")
                else:
                    instance = Cart.objects.create(user=user)
            else:
                return Response({"user": "User must be authenticated."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.queryset.filter(user=user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            serializer = self.serializer_class(data={'user':user.pk})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"user": "User must be authenticated."}, status=status.HTTP_400_BAD_REQUEST)

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [OrderPermission]