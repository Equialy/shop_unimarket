# Generated by Django 4.2.1 on 2024-09-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
