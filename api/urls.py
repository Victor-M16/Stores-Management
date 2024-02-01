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
]