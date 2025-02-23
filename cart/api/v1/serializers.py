from rest_framework import serializers
from ...models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = '__all__'

    def get_price(self,obj):
        return obj.price

    def get_total_price(self,obj):
        return obj.total_price
    
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ["user","created_at", "updated_at","status","total_price","items"]
