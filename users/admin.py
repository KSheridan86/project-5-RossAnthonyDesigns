from django.contrib import admin
from .models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ('email', 'created_on')
    list_display = ('email', 'created_on')
    search_fields = ('email', 'created_on')
