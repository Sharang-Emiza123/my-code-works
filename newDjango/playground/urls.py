from django.urls import path, include
from . import views

urlpatterns = [
    path('new/<int:pk>/', views.rdrct),
    path('', views.home),
]