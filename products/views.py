from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from products.models import Category, Products, BasketUser


# Create your views here.

def index(request):
    data = {
        'title': 'Unimarket'
    }
    return render(request, 'products/index.html', data)


def products(request):
    """ Категории на url proucts"""
    data = {
        'products': Products.objects.all(),
        'category': Category.objects.all(),
        'title': 'Товары'
    }

    return render(request, 'products/products.html', data)


def categories(request,category_slug):
    """Переход по выбранной категории"""
    category = get_object_or_404(Category, slug=category_slug)
    current_category = Category.objects.get(slug=category_slug)
    data = {
        'category': Category.objects.all(),
        'current_category': current_category,
        'products': Products.objects.filter(category = category),
        'title': 'Товары'
    }

    return render(request, 'products/products.html', data)

@login_required
def cart_item(request, slug_cart):
    """Описание карточки товара"""

    data = {
        'category': Category.objects.all(),
        'carts': Products.objects.filter(slug=slug_cart),
        'title':  'Товары'
    }
    return render(request, 'products/products.html', data)

@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    basket = BasketUser.objects.filter(user=request.user, product=product)
    if not basket.exists():
        BasketUser.objects.create(user=request.user, product=product,quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def basket_remove(request, basket_id):
    basket = BasketUser.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])