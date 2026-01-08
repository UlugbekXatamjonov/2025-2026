from django.contrib import admin
from .models import News
# Register your models here.


@admin.register(News)
class News_Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')
    list_filter = ('author', 'status', 'created_on')
    search_fields = ('title', 'body', 'tag')


