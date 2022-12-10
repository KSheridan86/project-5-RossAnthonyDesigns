from django.contrib import admin
from .models import Sculpture


@admin.register(Sculpture)
class SculptureAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'title', 'price')
    list_display = ('title', 'price', 'created_on')
    search_fields = ('title', 'price')
    ordering = ('-price',)
