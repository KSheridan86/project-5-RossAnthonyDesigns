
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('single_item/<str:pk>/', views.single_item, name="single_item"),
    path('add_sculpture/', views.add_sculpture, name="add_sculpture"),
    path('edit_sculpture/<str:pk>',
         views.edit_sculpture, name="edit_sculpture"),
    path('delete_sculpture/<str:pk>',
         views.delete_sculpture, name="delete_sculpture"),
]
