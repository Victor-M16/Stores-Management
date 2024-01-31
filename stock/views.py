from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *

# Create your views here.

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

