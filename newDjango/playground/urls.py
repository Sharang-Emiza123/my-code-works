from django.urls import path, include
from . import views

urlpatterns = {
    path('say/',views.say_hello),
}