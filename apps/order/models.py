from django.db import models

from apps.cart.models import ShoppingCart


class Order(models.Model):

    PAYMENT_CHOICES = (
        ("cash", "Наличные"),
        ("card", "Оплата картой"),
        ("debt", "В долг")
    )
    shopping_cart = models.ForeignKey(to=ShoppingCart, on_delete=models.PROTECT, related_name='order')
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    email = models.EmailField()
    payment_choice = models.CharField(choices=PAYMENT_CHOICES, max_length=15)
    order_coments = models.TextField(blank=True, null=True)
