# Generated by Django 4.2.1 on 2024-09-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Мужской'), (1, 'Женский')], null=True, verbose_name='Пол'),
        ),
    ]
