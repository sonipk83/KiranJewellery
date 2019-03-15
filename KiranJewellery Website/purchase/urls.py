from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewPurchase, name='purchase-view'),
    path('add/', views.addPurchase, name='purchase-add'),
]