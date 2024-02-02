from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


class StockInline(admin.StackedInline):
    model = Stock
    extra = 0


@admin.register(ProductInventory)
class ProductInventoryModelAdmin(admin.ModelAdmin):
    list_display = ['sku', 'upc']
    inlines = [StockInline]

class StockAdmin(admin.ModelAdmin):
    list_display = ('product_inventory', 'total_stock', 'units_out', 'last_checked')

admin.site.register(Stock, StockAdmin)
