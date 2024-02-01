from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.

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

