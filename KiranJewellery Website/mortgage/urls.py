from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateMortgageView,
    PostUpdateMortgageView,
    PostDeleteMortgageView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='mortgage-home'),
    path('mortgage/<int:pk>/', PostDetailView.as_view(), name='mortgage-detail'),
    path('mortgage/new/', PostCreateMortgageView.as_view(), name='mortgage-create'),
    path('mortgage/<int:pk>/update/', PostUpdateMortgageView.as_view(), name='mortgage-update'),
    path('mortgage/<int:pk>/delete/', PostDeleteMortgageView.as_view(), name='mortgage-delete'),
    path('about/', views.about, name='mortgage-about'),

]