from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="view_cart"),
    path('add/<item_id>/', views.add_to_cart, name="add_to_cart"),
    path('subtract/<item_id>/',
         views.subtract_from_cart, name="subtract_from_cart"),
    path('delete/<item_id>/',
         views.delete_item_from_cart, name="delete_item_from_cart"),
    path('delete_cart/', views.delete_cart, name="delete_cart"),
]
