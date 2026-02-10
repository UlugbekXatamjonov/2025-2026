from django.contrib import admin
from .models import New
# Register your models here.

@admin.register(New)
class New_Admin(admin.ModelAdmin):
    list_display = ('name', 'author', 'status', 'created_on')


