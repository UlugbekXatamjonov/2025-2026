from django.db import models

# Create your models here.

STATUS = (
    ("have", "Sotuvda"),
    ("have_not", "Sotuvda emas"),
)

class Category(models.Model):
    """  """
    name = models.CharField(max_length=250, verbose_name="Nomi")
    photo = models.ImageField(upload_to='category_photo', verbose_name="Rasm")
    
    status = models.CharField(max_length=10, choices=STATUS, default='have', verbose_name="Holati")
    
    def __str__(self):
        return self.name
    
class Meal(models.Model):
    """  """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=250, verbose_name="Nomi")
    photo = models.ImageField(upload_to='meal_photo', verbose_name="Rasm")
    description = models.TextField(verbose_name="Tarif")
    price = models.PositiveIntegerField(verbose_name="Narx")
    weight = models.CharField(max_length=255, verbose_name="Og'irlik/Litr/Portsia") 
    
    status = models.CharField(max_length=10, choices=STATUS, default='have', verbose_name="Holati")
    
    def __str__(self):
        return self.name


class Meal_type(models.Model):
    """  """
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='types', verbose_name="Taom")
    name = models.CharField(max_length=250, verbose_name="Nomi")
    price = models.PositiveIntegerField(verbose_name="Narx")
    
    status = models.CharField(max_length=10, choices=STATUS, default='have', verbose_name="Holati")
    
    def __str__(self):
        return self.name


class QR_code(models.Model):
    """  """
    name = models.CharField(max_length=250, verbose_name="Nomi")
    url = models.URLField(verbose_name="Sayt manzili")
    photo = models.ImageField(upload_to='qr_codes', verbose_name="QR code")
    
    def __str__(self):
        return self.name