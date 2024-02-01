from django.urls import path

from . import views

app_name = 'stock'


urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='products'),
    path('product-inventory/', views.ProductInventoryListAPIView.as_view(), name='product_inventory'),
    path('product-stock/', views.StockListAPIView.as_view(), name='product_stock'),
    path('inventory-update-view/<str:sku>/', views.ProductInventoryUpdateAPIView.as_view(), name='inventory-update-view'),
    # path('<str:sku>/update/', views.ProductInventoryUpdateAPIView.as_view(), name='inventory-update-view'),
]