from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('profiles/', profiles),
    path('profiles/<int:pk>', profile_detail),
]