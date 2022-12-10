
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('artist/', views.artist, name="artist")
]
