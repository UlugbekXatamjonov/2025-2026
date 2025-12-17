from django.contrib import admin
from .models import Cake, Category, New

# Register your models here.

@admin.register(Cake)
class Cake_Admin(admin.ModelAdmin):
    list_display = ('name', "category", 'price', 'status')
    list_filter = ('status', 'cretaed_on', 'category')
    search_fields = ('body', 'price', 'name')
    
@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ('name', "cretaed_on", 'status')
    list_filter = ('status', 'cretaed_on')
    search_fields = ('name', )
    
@admin.register(New)
class New_Admin(admin.ModelAdmin):
    list_display = ('title', "cretaed_on", 'status')
    list_filter = ('status', 'cretaed_on')
    search_fields = ('title', 'body')


