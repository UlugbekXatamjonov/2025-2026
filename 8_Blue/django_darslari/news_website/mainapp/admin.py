from django.contrib import admin
from .models import News

# Register your models here.

@admin.register(News)
class News_Admin(admin.ModelAdmin):
    list_display = ('title','author', 'status', 'created_on', 'views_count')
    list_filter = ('status', 'author', 'created_on')
    search_fields = ('title', 'body', 'read_time', 'views_count')
















