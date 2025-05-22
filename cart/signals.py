from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import CartItem

@receiver(pre_delete, sender=CartItem)
def mymodel_pre_delete(sender, instance, **kwargs):
    """
    Signal receiver function that runs before a MyModel instance is deleted.
    """
    print(f"Instance {instance} of {sender.__name__} is about to be deleted")
    instance.cart.total_price = instance.cart.total_price - instance.product.price * instance.quantity 
    instance.cart.save()