# Generated by Django 4.2.1 on 2024-09-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='slug_1', max_length=255, unique=True),
        ),
    ]
