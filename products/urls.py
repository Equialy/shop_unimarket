from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
app_name = 'products'
# Для кеширования отдельных страниц перед представлением прописать cache_page(30)(views.выбрать представление)
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('cats/<slug:category_slug>/', views.categories, name='categories'),
    path('products/<slug:slug_cart>/', views.cart_item, name='cart_item'),
    path('basket/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>/', views.basket_remove, name='basket_remove'),

]
