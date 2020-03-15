from django.urls import path, include
from rest_framework import routers
from .views import AuthRegister, AuthAccountInfo

urlpatterns = [
    path('register/', AuthRegister.as_view()),
    path('myinfo/', AuthAccountInfo.as_view()),
]
