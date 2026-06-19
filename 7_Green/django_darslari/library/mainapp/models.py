from django.db import models

# Create your models here.

TIL = (
    ('lotin',"Lotin"),
    ('kril', "Kril"),
    ('ingiliz', "Ingiliz tili"),
    ('rus', "Rus tili")
)


class Book(models.Model):
    nomi = models.CharField(max_length=100, unique=True)# 255
    narxi = models.PositiveIntegerField()
    isbn = models.PositiveIntegerField()
    yozuvi = models.CharField()
    yili = models.PositiveIntegerField()
    tili = models.CharField(choices=TIL)
    sahifalar_soni = models.PositiveIntegerField()
    nashiryot = models.CharField()
    muqova = models.CharField()
    tarjimonlar = models.CharField()
    yulduzlar = models.CharField() # 5 ta
    rasm = models.ImageField()
    kitob_haqida = models.TextField()
    muallif = models.CharField()
    turi = models.CharField() # kitob turi

    qoshilgan_vaqt = models.DateTimeField()
    status = models.BooleanField()














