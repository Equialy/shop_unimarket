from django.contrib import admin

from products.models import Products, Category


# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'time_create', 'image', 'count', 'category']
    list_display = ['title', 'time_create', 'image', 'count', 'category']
    list_display_links = ('title',)
    readonly_fields = ('time_create',)
    search_fields = ('title', 'time_create',)
    list_filter = ['category']
    list_editable = ['category']
    list_per_page = 5
    list_max_show_all = 100





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']