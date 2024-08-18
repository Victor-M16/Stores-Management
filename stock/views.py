import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from channels.layers import get_channel_layer

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from asgiref.sync import async_to_sync

from .models import *
from .serializers import *
# views.py


from .models import ProductInventory, Stock

# @csrf_exempt
# def update_product_inventory(request, sku):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))

#         # Assuming your request payload looks like {'total_stock': 50}
#         new_total_stock = data.get('total_stock')

#         if new_total_stock is not None:
#             product_inventory = get_object_or_404(ProductInventory, sku=sku)
#             stock_instance, created = Stock.objects.get_or_create(product_inventory=product_inventory)

#             # Update the total_stock field
#             stock_instance.total_stock = new_total_stock
#             stock_instance.save()

#             # Send real-time update to WebSocket consumers
#             channel_layer = get_channel_layer()
#             async_to_sync(channel_layer.group_send)(
#                 f"product_inventory_{sku}",
#                 {
#                     'type': 'product_inventory.update',
#                     'message': f'Total stock updated to {new_total_stock}!',
#                 }
#             )

#             return JsonResponse({'message': 'Product inventory updated successfully!'})
#         else:
#             return JsonResponse({'error': 'Invalid request payload.'}, status=400)

#     return JsonResponse({'error': 'Invalid request method.'}, status=400)



# Create your views here.


class RFIDDataView(APIView):
    def post(self, request, format=None):
        serializer = RFIDDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# stock/views.py

class ProductInventoryUpdateAPIView(APIView):
    def patch(self, request, sku):
        try:
            product_inventory = ProductInventory.objects.get(sku=sku)
        except ProductInventory.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductInventoryUpdateSerializer(product_inventory, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockListAPIView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = ProductInventoryStockSerializer
    permission_classes = [AllowAny]


class ProductInventoryListAPIView(generics.ListAPIView):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    permission_classes = [AllowAny]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]




# class ProductInventoryUpdateAPIView(generics.UpdateAPIView):
#     queryset = ProductInventory.objects.all()
#     serializer_class = ProductInventorySerializer
#     lookup_field = 'sku'

#     def perform_update(self, serializer):
#         instance = serializer.save()



# Views
def index(request):

    inventory = ProductInventory.objects.all().order_by('-updated_at')[:3]
    reorder_points = ['189.2', '185.8', '136.2']
    inventory_list = []
    for product, reorder in zip(inventory, reorder_points):
        data = {
            'product': product,
            'reorder': reorder,
        }
        inventory_list.append(data)

    context = {
        'inventory': inventory_list,
    }

    if request.htmx:
        return render(request, 'stock/partials/data-partial.html', context)

    return render(request, 'stock/index.html', context)