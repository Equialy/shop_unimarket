from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('cats/<slug:category_slug>/', views.categories, name='categories'),
    path('products/<slug:slug_cart>/', views.cart_item, name='cart_item'),

]
