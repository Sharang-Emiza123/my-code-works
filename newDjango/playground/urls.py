from django.urls import path
from . import views

urlpatterns = {
    path('say/',views.say_hello),
    path('ter/', views.terminated)
}