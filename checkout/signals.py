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
            'Hey Ross dude,\
            someone liked your stuff enough to part with actual cash, WooHoo!',
            settings.EMAIL_HOST_USER,
            ['kensheridan86@gmail.com'],
            fail_silently=False,)


@receiver(post_save, sender=Order)
def order_confirmation(sender, instance, created, **kwargs):
    order_number = Order.objects.all().order_by(
            '-date').values_list('order_number', flat=True)[0:1]
    name = Order.objects.all().order_by(
            '-date').values_list('full_name', flat=True)[0:1]
    email = Order.objects.all().order_by(
            '-date').values_list('email', flat=True)[0:1]
    line = '\n'
    send_mail(
            'Thank you for your order!',
            f'\
            Hi {name[0]},{line}\
            {line}\
            Thank you for your order, {line}\
            Your order number is {order_number[0]}, {line}\
            If you have any questions, {line}\
            Please, feel free to contact us and we will be happy to help. {line}\
            Please quote your order number in any correspondence. {line}\
            {line}\
            Kind Regards, {line}\
            The Forged Nature Team.',
            settings.EMAIL_HOST_USER,
            [email[0]],
            fail_silently=False,)
