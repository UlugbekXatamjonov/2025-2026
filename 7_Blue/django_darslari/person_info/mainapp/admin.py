from django.contrib import admin
from .models import Person

# Register your models here.

@admin.register(Person)
class Person_Admin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birth_date', 'adress', 'created_on')
    list_filter = ('gender', 'created_on', 'job')
    search_fields = ('name', 'surname', 'adress', 'about')









    