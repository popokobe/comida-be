from django.urls import path, include
from rest_framework import routers
from .views import AuthRegister

urlpatterns = [
    path('register/', AuthRegister.as_view())
]
