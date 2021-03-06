from django.db import models
from django.conf import settings

from apps.product.models import Product


class ShoppingCart(models.Model):
    """
    Корзина пользователя
    """
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'cart_id: {self.id} owner: {self.user}'


class CartItem(models.Model):
    """
    Предмет в корзине
    """
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True, related_name='product_in_cart')
    cart_shopping = models.ForeignKey(to=ShoppingCart, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f'{self.id} {self.cart_shopping.user.username}'