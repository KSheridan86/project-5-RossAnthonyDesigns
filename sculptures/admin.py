from django.contrib import admin
from .models import Sculpture


@admin.register(Sculpture)
class SculptureAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'title')
    list_display = ('title', 'created_on')
    search_fields = ('title',)
