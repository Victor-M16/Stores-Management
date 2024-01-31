from django.urls import path

from . import views

app_name = 'stock'


urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='products'),
    path('product-inventory/', views.ProductInventoryListAPIView.as_view(), name='product_inventory'),
    path('product-stock/', views.StockListAPIView.as_view(), name='product_stock'),
]