# Generated by Django 4.2.1 on 2024-09-21 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
    ]
