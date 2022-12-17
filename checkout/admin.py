from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total')
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total')
    list_filter = ('date', 'full_name', 'country', 'grand_total')
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total')
    search_fields = ('order_number', 'date', 'full_name',
                     'email', 'phone_number', 'country',
                     'order_total', 'grand_total')
    ordering = ('-date',)
