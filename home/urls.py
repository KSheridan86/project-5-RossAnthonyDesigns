
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('artist/', views.artist, name="artist"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('order_summary/<uuid:order_number>', views.order_summary, name="order_summary"),
    path('gallery/', views.gallery, name="gallery"),
]
