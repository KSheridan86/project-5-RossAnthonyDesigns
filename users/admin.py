from django.contrib import admin
from .models import Newsletter, Message, Review


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ('email', 'created_on')
    list_display = ('email', 'created_on')
    search_fields = ('email', 'created_on')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'created_on')
    list_display = ('name', 'email', 'created_on')
    search_fields = ('name', 'email', 'created_on')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_on')
    list_display = ('name', 'created_on')
    search_fields = ('name', 'created_on')
