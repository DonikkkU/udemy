# Generated by Django 4.1 on 2022-10-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profiles_teachers_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='social_facebook',
            field=models.URLField(blank=True, default='instagram', max_length=100, null=True),
        ),
    ]
