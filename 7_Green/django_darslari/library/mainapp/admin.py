from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class Book_Admin(admin.ModelAdmin):
    list_display = ('nomi', 'muallif', "narxi")

