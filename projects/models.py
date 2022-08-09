from users.models import Profiles
from django.db import models
import os
from rest_framework.exceptions import ValidationError



class Course(models.Model):
    name = models.CharField(blank=True, max_length=200, null=False)
    about = models.TextField(blank=True, max_length=500, null=False)
    image = models.ImageField(blank=True, null=False, upload_to='course', default='empty.png')
    rate = models.IntegerField(default=0)
    vote_count = models.IntegerField(default=0)
    author = models.ForeignKey(Profiles, blank=True, null=True, on_delete=models.SET_NULL, related_name='author')
    price = models.DecimalField(max_digits=6, blank=True, null=False, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(blank=True, max_length=200, null=False)
    definition = models.CharField(blank=True, max_length=200, null=False)

    def __str__(self):
        return f'{self.name}'
