from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class GenderChoice(models.IntegerChoices):
        male = 0, 'Мужской'
        female = 1, 'Женский'

    image = models.ImageField(upload_to='images_users', null=True, blank=True, verbose_name='Фото')
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.IntegerField(choices=GenderChoice.choices, null=True,verbose_name = 'Пол')
