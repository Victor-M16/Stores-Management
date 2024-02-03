from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('procurement/choice/', views.ProcurementChoiceView.as_view(), name='procurement-choice'),
    path('tender/notice/', views.TenderNoticeView.as_view(), name='tender-notice'),
    path('bid/', views.BidView.as_view(), name='bid'),
    path('contract/', views.ContractView.as_view(), name='contract'),
    path('procurement/process/', views.ProcurementProcessView.as_view(), name='procurement-process'),
    path('procurement/act/', views.PublicProcurementActView.as_view(), name='act'),

    path('create_rfq/', views.CreateRFQAPIView.as_view(), name='create_rfq_api'),
    path('apply_to_rfq/', views.ApplyToRFQAPIView.as_view(), name='apply_to_rfq_api'),
    path('open_rfqs/', views.OpenRFQsAPIView.as_view(), name='open_rfqs_api'),


    path('inventory_metrics/', views.InventoryMetricsView.as_view(), name='inventory_metrics'),
    path('product_sku_dict/',views.ProductSkuDictView.as_view(), name='product-sku-dict-view'),
]

