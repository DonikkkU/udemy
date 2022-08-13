# Generated by Django 4.1 on 2022-08-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profiles_full_name'),
        ('projects', '0002_alter_course_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('duration', models.IntegerField(default=40)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_theme', to='projects.course')),
            ],
        ),
        migrations.CreateModel(
            name='Theme_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dictionary', models.FileField(blank=True, upload_to='homework_dict')),
                ('conversation', models.FileField(blank=True, upload_to='homework_conv')),
                ('translation', models.FileField(blank=True, upload_to='homework_translation')),
                ('exercise', models.ImageField(blank=True, upload_to='homework_ex')),
                ('comment', models.CharField(max_length=50, null=True)),
                ('is_available', models.BooleanField(default=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='theme_user', to='users.profiles')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='theme', to='projects.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_id', to='projects.course')),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students_course', to='projects.course')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100, null=True)),
                ('is_done', models.BooleanField(blank=True, default=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_homework', to='users.profiles')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='homeworks', to='projects.theme')),
            ],
        ),
    ]
