from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('course/', CourseView.as_view()),
    path('course/<int:pk>', CourseDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CourseDetailView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:pk>', OrderDetailView.as_view()),
    path('homework/', HomeworkView.as_view()),
    path('homework/<int:pk>', HomeworkDetailView.as_view()),
    path('theme/', ThemeView.as_view()),
    path('theme/<int:pk>', ThemeDetailView.as_view()),
    path('themeuser/', ThemeUserView.as_view()),
    path('themeuser/<int:pk>', ThemeDetailView.as_view())
]