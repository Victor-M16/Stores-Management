from rest_framework import serializers

from .models import *

class RFIDDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFIDData
        fields = ('uid',)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['web_id', 'name', 'slug', 'is_active', 'created_at', 'updated_at']


class ProductInventoryStockSerializer(serializers.ModelSerializer):

    # product_inventory = ProductInventorySerializer(many=True)

    class Meta:
        model = Stock
        fields = ['last_checked', 'total_stock', 'units_out',]


class ProductInventorySerializer(serializers.ModelSerializer):

    product_inventory = ProductInventoryStockSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='stock:inventory-update-view',
        lookup_field='sku',
        )

    class Meta:
        model = ProductInventory
        fields = ['url', 'sku', 'upc', 'product', 'product_inventory', 'product_variant', 'is_active', 'purchase_cost', 'initial_stock', 'last_ordered', 'created_at', 'updated_at']

    # def update(self, instance, validated_data):
    #     # Set partial=True if needed
    #     return super().update(instance, validated_data, partial=True)
        
class ProductInventoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInventory
        fields = ['sku', 'upc', 'product', 'product_variant', 'is_active', 'purchase_cost', 'initial_stock', 'last_ordered', 'created_at', 'updated_at']
    