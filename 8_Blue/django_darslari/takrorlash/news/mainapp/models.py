from django.db import models

# Create your models here.


class New(models.Model):
    name = models.CharField(max_length=100, verbose_name="Sarlavha", unique=True)
    body = models.TextField(verbose_name='Matn')
    author = models.CharField(max_length=100, default="Q. Abdurahmon")
    tag = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    views_count = models.PositiveIntegerField(default=1)

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.name
        return f"{self.name} - {self.author}"




