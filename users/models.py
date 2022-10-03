

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
import os
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from projects.models import *





class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ROLE=(
        ("teacher", "teacher"),
        ("student", "student"),
        ("admin", "admin")
    )
    full_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, choices=ROLE)
    image = models.ImageField(blank=True, null=False, upload_to='portfolio')
    comment_count = models.IntegerField(default=0)
    students_count = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    about = models.TextField(max_length=1000, blank=True, null=False)
    social_facebook = models.URLField(max_length=100, blank=True, null=True)
    social_youtube = models.URLField(blank=True, null=True)
    social_telegram = models.URLField(blank=True, null=True)
    social_instagram = models.URLField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    teachers_bio = models.TextField(max_length=500, blank=True, null=True)


    def __str__(self):
        return f'{self.full_name}'

