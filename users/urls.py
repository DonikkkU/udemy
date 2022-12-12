from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('profiles/', ProfilesView.as_view()),
    path('profiles/<int:pk>', ProfilesDetailView.as_view()),
    path('teachers/', TeachersView.as_view()),
    path('teachers/<int:pk>', TeachersDetailView.as_view()),
    path('send/', send_sms),
    path('login/', login_user),
    path('logout/', logout_user),
    path('register/', register_user)

]