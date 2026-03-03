from django.db import models

# Create your models here.

APPLICATION_STATUS = (
    ("qabul_qilingan","Qabul qilingan"), 
    ("organilib_chiqilmoqda","O'rganilib chiqilmoqda"), 
    ("rad_etilgan","Rad etilgan"), 
    ("hal_qilingan","Hal qilingan")
)


class Category(models.Model):
    """  """
    name = models.CharField(max_length=50, verbose_name="Nomi", unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Application(models.Model):
    """  """
    name = models.CharField(max_length=50, verbose_name="Nomi", unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="applications")
    body = models.TextField(verbose_name="Batafsil")
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    applicant = models.CharField(max_length=40, verbose_name="Arizachi")
    phone1 = models.CharField(max_length=13, verbose_name="Tel. raqam 1") # regex
    phone2 = models.CharField(max_length=13, verbose_name="Tel. raqam 2", null=True, blank=True) # regex
    
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS, default="qabul_qilingan")

    def __str__(self):
        return self.name
    

