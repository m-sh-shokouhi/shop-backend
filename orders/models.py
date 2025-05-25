from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from products.models import Product  # Assuming you have a Product model

class Order(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created', _('Created')
        PROCESSING = 'processing', _('Processing')
        SHIPPED = 'shipped', _('Shipped')
        DELIVERED = 'delivered', _('Delivered')
        CANCELLED = 'cancelled', _('Cancelled')
        REFUNDED = 'refunded', _('Refunded')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )

    transaction_id = models.CharField(max_length=100, unique=True)
    
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField(blank=True, null=True)
    
    payment_method = models.CharField(max_length=50)
    shipping_method = models.CharField(max_length=50)
    shipping_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"

    @property
    def total_cost(self):
        items_cost = sum(item.get_cost() for item in self.items.all())
        return items_cost + self.shipping_cost + self.tax - self.discount


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    quantity = models.PositiveIntegerField(default=1)
    variant = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"

    def get_cost(self):
        return self.price * self.quantity
    

