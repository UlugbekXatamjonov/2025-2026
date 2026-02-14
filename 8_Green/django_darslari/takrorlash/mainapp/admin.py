from django.contrib import admin
from .models import New


# Register your models here.


@admin.register(New)
class New_Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'tag', 'status', 'created_on')
    list_filter = ('author', 'tag', 'status', 'created_on') # kam uchraydigan ma'umotlar
    search_fields = ('title', 'body')# xar-xil bo'ladigan ma'umotlar

