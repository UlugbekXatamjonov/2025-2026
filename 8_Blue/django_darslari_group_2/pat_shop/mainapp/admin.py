from django.contrib import admin
from .models import Pat
# Register your models here.

@admin.register(Pat)
class Pat_Admin(admin.ModelAdmin):
    list_display = ('zoti', 'laqabi', 'jinsi', 'narxi', 'created_on')
