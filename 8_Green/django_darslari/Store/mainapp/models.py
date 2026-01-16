from django.db import models

# Create your models here.

color = (
    ('black',"Qora"),
    ('white',"Oq"),
    ('green',"Yashil"),
    ('blue',"Ko'k"),
    ('yellow',"Sariq"),
    ('pink',"Pushti"),
)


class Category(models.Model):
    """  """
    name = models.CharField(max_length=100, verbose_name="Nomi")
    photo = models.ImageField(verbose_name="rasmi")
    
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    """   """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50, choices=color)
    
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    