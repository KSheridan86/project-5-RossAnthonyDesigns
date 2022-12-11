
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('single_item/<str:pk>/', views.single_item, name="single_item"),
]
