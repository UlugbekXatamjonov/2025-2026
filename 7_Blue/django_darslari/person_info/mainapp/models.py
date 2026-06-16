from django.db import models

# Create your models here.

GENDER = (
    ('male', "Erkak"),
    ('famale', "Ayol")
)


class Person(models.Model):
    name = models.CharField(max_length=50, unique=True) # unique - yagonalilik
    surname = models.CharField(max_length=50) # max_length - maksimal uzunlik
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER, default='male') # choises - tanlanadigan qilish
    photo = models.ImageField(upload_to="person_photos/", null=True, blank=True)# upload_to - rasmlarni tushish joyi
    adress = models.TextField()
    job = models.CharField(max_length=100, default="Bekorchi")
    about = models.TextField(null=True, blank=True)
    
    status = models.BooleanField()  # True / False
    created_on = models.DateTimeField(auto_now_add=True)











