from django.contrib import admin
from .models import Category, Meal, Meal_type, QR_code

# Register your models here.

@admin.register(Category)
class  Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)

@admin.register(Meal)
class  Meal_Admin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'status')
    list_filter = ('status', 'category')
    search_field = ('name', 'description', 'price')

@admin.register(Meal_type)
class  Meal_type_Admin(admin.ModelAdmin):
    list_display = ('name', 'meal', 'price', 'status')
    list_filter = ('status', 'meal')
    search_field = ('price',)

@admin.register(QR_code)
class  QR_code_Admin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_filter = ('status',)

