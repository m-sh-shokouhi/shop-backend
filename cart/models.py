from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def save(self, *args, **kwargs):
        # TODO: Here must check the quantity to not be more than product stock available
        if self.pk:
            old_instance = CartItem.objects.get(pk=self.pk) 
            self.cart.total_price = self.cart.total_price + (self.quantity - old_instance.quantity) * self.product.price
            self.cart.save()
        else:
            self.cart.total_price = self.cart.total_price + self.quantity * self.product.price
            self.cart.save()
        super().save(*args,**kwargs)
    
    @property
    def price(self):
        return self.product.price
    
    @property
    def total_price(self):
        return self.product.price * self.quantity