from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=255,null=True,default='slug_1', unique=True,  db_index=True)
    count = models.PositiveIntegerField(default=0, verbose_name='Колличество')
    image = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='product',
                                 verbose_name='Категория')

    # def __str__(self):
    #     return f'Продукт: {self.title} | Категория: {self.category.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Products, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-time_create']




class Category(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return f'{self.name}'

