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
    course_id = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course_id')
    course_category = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course_category')
    student_id = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='students_course')
    bought_at = models.DateField(auto_now_add=True)


class Homework(models.Model):
    student = models.ForeignKey(Profiles, on_delete=models.SET_NULL, related_name='student_homework')
    comment = models.CharField(max_length=100)
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, related_name='homeworks')
    is_done = models.BooleanField(blank=True, null=False)
    # dictionary - fayl
    # conversation - fayl
    # translation - fayl
    # exercise - rasm


class Theme(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course_theme')


class Theme_user(models.Model):
    student = models.ForeignKey(Profiles, on_delete=models.SET_NULL, related_name='theme_user')
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, related_name='theme')


