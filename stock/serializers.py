from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['web_id', 'name', 'slug', 'is_active', 'created_at', 'updated_at']


class ProductInventoryStockSerializer(serializers.ModelSerializer):

    # product_inventory = ProductInventorySerializer(many=True)

    class Meta:
        model = Stock
        fields = ['last_checked', 'units', 'units_out',]


class ProductInventorySerializer(serializers.ModelSerializer):

    product_inventory = ProductInventoryStockSerializer()
    product = ProductSerializer()

    class Meta:
        model = ProductInventory
        fields = ['sku', 'upc', 'product', 'product_inventory', 'product_variant', 'is_active', 'purchase_cost', 'initial_stock', 'last_ordered', 'created_at', 'updated_at']
