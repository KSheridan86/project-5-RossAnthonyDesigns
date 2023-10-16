from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .models import OrderLineItem, Order
from sculptures.models import Sculpture


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()


@receiver(post_save, sender=Order)
def new_order(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Order',
            f"Hey Ross dude,"
            f"\n\n"
            f"Someone liked your stuff enough to part with actual cash!"
            f"\n\n"
            f"Log in and check out the order."
            f"\n\n"
            f"Peace!",
            settings.EMAIL_HOST_USER,
            ['forged.nature.irl@gmail.com'],
            fail_silently=False,)
