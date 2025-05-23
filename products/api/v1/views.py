from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Category, Product, ProductImage
from .permissions import ReadOnlyForUsers
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyForUsers]
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [field.name for field in Category._meta.get_fields()]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ReadOnlyForUsers]
    # lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [field.name for field in Product._meta.get_fields()]

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [ReadOnlyForUsers]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [field.name for field in ProductImage._meta.get_fields()]
