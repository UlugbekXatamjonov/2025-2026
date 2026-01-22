from django.db import models

# Create your models here.

STATUS = (
    ('ended', "Sotuvda tugagan"),
    ('have', "Sotuvda"),
    ('arxive', "Sotuvdan olib tashlangan")
)

NEW_STATUS = (
    ('active', "Faol"),
    ('deactive', "Faolemas ❌")
)


class Category(models.Model):
    """ Tort va shirinliklar uchun kategoriya(bo'lim) """

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/category_photos")
    
    cretaed_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default='have')

    def __str__(self):
        return self.name
    

class Cake(models.Model): # 
    """  """
    
    name = models.CharField()
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE, 
                                 related_name="cakes") 
    body = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="photos/cake_photos")

    cretaed_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default='have')

    def __str__(self):
        return self.name


class New(models.Model):
    """ Yabgiliklar uchun model 
    
    title - yangilikning nomi
    body - yangilikning matni
    image - rasm
    
    """

    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    body = models.TextField(verbose_name="Matn")
    image = models.ImageField(upload_to='photos/news_photos', verbose_name="Rasm")

    cretaed_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=NEW_STATUS, default='active', verbose_name="Holati")

    def __str__(self):
        return self.title


class Branch(models.Model):
    """ Filiallar uchun model """

    name  = models.CharField(max_length=250, verbose_name="Nomi")
    adress = models.CharField(max_length=255, verbose_name="Manzil")
    work_time = models.CharField(max_length=255, verbose_name="ish vaqti")
    phone = models.CharField(max_length=255, verbose_name="Tel.n raqam")
    map_adress = models.CharField(max_length=255, verbose_name="Xarita manzili")

    cretaed_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=NEW_STATUS, default='active', verbose_name="Holati")

    def __str__(self):
        return self.name













