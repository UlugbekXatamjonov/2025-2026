from django.contrib import admin
from .models import Category, Book, Author

# Register your models here.

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status', )

@admin.register(Author)
class Author_Admin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status', )

@admin.register(Book)
class Book_Admin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'language', 'publisher', 'status')
    list_filter = ('status', 'category', 'author', 'language')
    search_fields = ('name', 'about')

    