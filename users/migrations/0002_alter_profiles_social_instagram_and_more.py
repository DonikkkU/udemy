# Generated by Django 4.1.1 on 2022-09-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='social_instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='social_telegram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='social_youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
