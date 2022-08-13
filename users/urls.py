from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('profiles/', ProfilesView.as_view()),
    path('profiles/<int:pk>', ProfilesDetailView.as_view()),
]