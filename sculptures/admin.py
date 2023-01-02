from django.contrib import admin
from .models import Sculpture


@admin.register(Sculpture)
class SculptureAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'title', 'price', 'available', 'quantity')
    list_display = ('title', 'price', 'created_on', 'available', 'quantity')
    search_fields = ('title', 'price', 'available', 'quantity')
    ordering = ('-price',)
