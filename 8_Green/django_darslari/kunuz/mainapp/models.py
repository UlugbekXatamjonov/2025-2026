from django.db import models

# Create your models here.

class News(models.Model):
    """ Yangiliklar uchun klass """
    
    title = models.CharField(max_length=255) # qisqa matnlar uchun max -> 255  | sarlavha 
    body = models.TextField() # yangilikning matni uchun
    photo = models.ImageField() # rasm uchun ! pip install pillow
    video = models.FileField() # video uchun
    views_count = models.PositiveIntegerField()
    time_to_read = models.PositiveIntegerField()
    tag = models.CharField(max_length=50) # #tag uchun
    author = models.CharField(max_length=100) # muallif

    created_on = models.DateTimeField(auto_now_add=True) # yozilgan vaqti
    status = models.BooleanField(default=True) # Holati










