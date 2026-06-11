from django.db import models

# Create your models here.

class Book(models.Model):
    nomi = models.CharField()# 255
    narxi = models.PositiveIntegerField()
    isbn = models.PositiveIntegerField()
    yozuvi = models.CharField()
    yili = models.PositiveIntegerField()
    tili = models.CharField()
    sahifalar_soni = models.PositiveIntegerField()
    nashiryot = models.CharField()
    muqova = models.CharField()
    tarjimonlar = models.CharField()
    yulduzlar = models.CharField()
    rasm = models.ImageField()
    kitob_haqida = models.TextField()
    muallif = models.CharField()
    turi = models.CharField()

    qoshilgan_vaqt = models.DateTimeField()
    status = models.BooleanField()














