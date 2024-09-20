from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from products.models import Category, Products


# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(request):
    """ Категории на url proucts"""
    data = {
        'products': Products.objects.all(),
        'category': Category.objects.all(),
    }

    return render(request, 'products/products.html', data)


def categories(request,category_slug):
    """Переход по выбранной категории"""
    category = get_object_or_404(Category, slug=category_slug)
    current_category = Category.objects.get(slug=category_slug)
    data = {
        'category': Category.objects.all(),
        'current_category': current_category,
        'products': Products.objects.filter(category = category)
    }

    return render(request, 'products/products.html', data)


def cart_item(request, slug_cart):
    """Описание карточки товара"""
    data = {
        'category': Category.objects.all(),
        'carts': Products.objects.filter(slug=slug_cart)
    }
    return render(request, 'products/products.html', data)
