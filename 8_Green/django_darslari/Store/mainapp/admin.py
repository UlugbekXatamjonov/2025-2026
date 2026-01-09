from django.contrib import admin
from .models import Category, Product


# Register your models here.

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'status')


@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'color')




