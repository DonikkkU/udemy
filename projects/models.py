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
    price = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(blank=True, max_length=200, null=False)
    definition = models.CharField(blank=True, max_length=200, null=False)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course_id', null=True)
    student_id = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='students_course', null=True)
    bought_at = models.DateTimeField(auto_now_add=True, null=True)



class Homework(models.Model):
    student = models.ForeignKey(Profiles, on_delete=models.SET_NULL, related_name='student_homework', null=True)
    comment = models.CharField(max_length=100, null=True)
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, related_name='homeworks', null=True)
    # check = models.ForeignKey('Theme_user', on_delete=models.SET_NULL, related_name='checkup', null=True)
    is_done = models.BooleanField(blank=True, null=False, default=False)

    def __bool__(self):
        return f'{self.is_done}'



class Theme(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course_theme', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    duration = models.IntegerField(default=40)

    def __str__(self):
        return f'{self.name}'


class Theme_user(models.Model):
    student = models.ForeignKey(Profiles, on_delete=models.SET_NULL, related_name='theme_user', null=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, related_name='theme', null=True)
    dictionary = models.FileField(blank=True, null=False, upload_to='homework_dict')
    conversation = models.FileField(blank=True, null=False, upload_to='homework_conv')
    translation = models.FileField(blank=True, null=False, upload_to='homework_translation')
    exercise = models.ImageField(blank=True, null=False, upload_to='homework_ex')
    comment = models.CharField(max_length=50, null=True)
    is_available = models.BooleanField(default=False)