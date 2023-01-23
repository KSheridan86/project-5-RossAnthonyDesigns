from django.urls import path
from . import views

urlpatterns = [
     path('', views.newsletter, name='newsletter'),
     path('message/', views.message, name='message'),
     path('leave_review/', views.leave_review, name="leave_review"),
     path('delete_newsletter/<str:pk>/',
          views.delete_newsletter, name="delete_newsletter"),
     path('view_message/<str:pk>', views.view_message, name="view_message"),
     path('view_review/<str:pk>', views.view_review, name="view_review"),
     path('delete_review/<str:pk>', views.delete_review, name="delete_review"),
     path('delete_message/<str:pk>',
          views.delete_message, name="delete_message"),
     path('delete_user', views.delete_user, name='delete_user'),
]
