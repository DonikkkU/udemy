# Generated by Django 4.1 on 2022-12-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=998, max_length=14, unique=True),
        ),
    ]
