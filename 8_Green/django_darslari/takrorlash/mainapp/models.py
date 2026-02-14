from django.db import models

# Create your models here.

class New(models.Model):
    """
    default = ""    -> standart qiymat
    null = True     -> Maydonni bo'sh qoldiradi 
    blank = True    -> Maydonni bo'sh qoldiradi
    unique = True   -> Shu maydonni yagona 
    
    """
    title = models.CharField(max_length=250, unique=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    tag = models.CharField(max_length=100)
    views_count = models.PositiveIntegerField(default=1)
    author = models.CharField(max_length=50, default="Sobirjonova Z.")
    like = models.PositiveIntegerField(blank=True, null=True)
    
    status = models.BooleanField(default=True) # True / False
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
















