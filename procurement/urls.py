from django.urls import path
from . import views

app_name = 'procurement'

urlpatterns = [
    path('', views.procurement_choice_view, name='procurement_choice'),
    path('tendering/', views.tendering_view, name='tendering'),
]