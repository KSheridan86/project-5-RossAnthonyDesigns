from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('message/', views.message, name='message'),
    path('leave_review/', views.leave_review, name="leave_review"),
]
