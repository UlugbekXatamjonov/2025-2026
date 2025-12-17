from django.db import models

# Create your models here.


class News(models.Model):
    """  """
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField()
    video = models.FileField()
    views_count = models.PositiveIntegerField(default=0)
    read_time = models.PositiveIntegerField()
    author = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
















