from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Message, Review


@receiver(post_save, sender=Message)
def new_private_message(sender, instance, created, **kwargs):
    email = Message.objects.values_list('email', flat=True)[0:1]
    sender = Message.objects.values_list('name', flat=True)[0:1]
    if created:
        send_mail('New Message',
                  f'A new private message has been received from {sender[0]}.',
                  email[0],
                  ['kensheridan86@gmail.com'],
                  fail_silently=False,)


@receiver(post_save, sender=Review)
def new_review(sender, instance, created, **kwargs):
    name = Review.objects.values_list('name', flat=True)[0:1]
    email = Review.objects.values_list('email', flat=True)[0:1]
    if created:
        send_mail('New Review',
                  f'{name[0]} has submitted a review for consideration',
                  email[0],
                  ['kensheridan86@gmail.com'],
                  fail_silently=False,)
