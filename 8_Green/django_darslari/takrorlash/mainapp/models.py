from django.db import models

# Create your models here.

class New(models.Model):
    """  """
    title = models.CharField(max_length=250)
    body = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    video = models.FileField(upload_to='videos/')
    tag = models.CharField(max_length=100)
    views_count = models.PositiveIntegerField(default=1)
    author = models.CharField(max_length=50, default="Sobirjonova Z.")
    like = models.PositiveIntegerField(blank=True, null=True)
    
    status = models.BooleanField(default=True) # True / False
    created_on = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.title} - {self.author}"





