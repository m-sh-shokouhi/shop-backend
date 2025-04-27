from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from ...models import Category, Product, ProductImage

class CategorySerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
