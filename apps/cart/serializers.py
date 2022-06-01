from rest_framework import serializers

from .models import CartItem, ShoppingCart


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')

    def validate(self, attrs):
        cart_shopping = self.context.get('request').user.cart
        attrs['cart_shopping'] = cart_shopping
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = instance.product.title
        return rep


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def to_representation(self, instance: ShoppingCart):
        rep = super().to_representation(instance)
        rep['products'] = CartItemSerializer(instance.cart_item.all(), many=True).data
        rep['total_price'] = instance.get_total_price_all()
        return rep