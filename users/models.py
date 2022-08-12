
from django.db import models
import os
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User




class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    social_facebook = models.URLField(max_length=100, blank=True, null=True)
    social_youtube = models.URLField(max_length=100, blank=True, null=True)
    social_telegram = models.URLField(max_length=100, blank=True, null=True)
    social_instagram = models.URLField(max_length=100, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    ROLE=(
        ("teacher", "teacher"),
        ("student", "student"),
        ("admin", "admin")
    )
    user_username = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, choices=ROLE)
    image = models.ImageField(blank=True, null=False, upload_to='portfolio')
    comment_count = models.IntegerField(default=0)
    students_count = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    about = models.TextField(max_length=1000, blank=True, null=False)

    def __str__(self):
        return f"{self.user_username}"



