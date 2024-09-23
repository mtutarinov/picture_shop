from django.contrib import admin

from .models import Order, OrderPainting


class OrderPaintingInline(admin.TabularInline):
    model = OrderPainting
    raw_id_fields = ['painting']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderPaintingInline]
