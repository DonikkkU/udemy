from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('course/', course),
    path('course/<int:pk>', course_detail),
    path('category/', category),
    path('category/<int:pk>', category_detail),
]