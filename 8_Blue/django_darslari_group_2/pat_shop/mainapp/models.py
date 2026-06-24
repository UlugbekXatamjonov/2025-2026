from django.db import models

# Create your models here.

GENDER = (
    ('boy', "O'g'il bola"),
    ('girl', "Qiz bola")
)

LOTOK = (
    ('yes', "Ha biladi"),
    ('no', "Yo'q bilmaydi")
)

class Pat(models.Model):
    zoti = models.CharField(max_length=25) # 255
    rasm = models.ImageField(upload_to="pats_photo/")
    laqabi = models.CharField()
    yoshi = models.CharField()
    jinsi = models.CharField(choices=GENDER)
    sogligi = models.CharField()
    manzil = models.CharField()
    narxi = models.CharField()
    telegram = models.CharField()
    telefon = models.CharField()
    lotok = models.CharField(choices=LOTOK)

    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
