from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField()  # Kichik matnlar - 255
    news_type = models.CharField()
    views_count = models.PositiveIntegerField() # Musbat sonlar uchun 
    body = models.TextField() # Katta matnlar uchun
    photo = models.ImageField() # Rasm uchun maydon
    video = models.FileField() # video, fayllar uchun
    author = models.CharField()

    created_on = models.DateTimeField() # Sana va vaqt uchun


























