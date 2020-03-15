from django.urls import path, include
from rest_framework import routers
from .views import AuthRegister, AuthAccountInfo

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', AuthRegister.as_view()),
    path('myinfo/', AuthAccountInfo.as_view()),
]
