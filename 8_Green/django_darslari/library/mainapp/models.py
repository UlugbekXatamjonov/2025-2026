from django.db import models

# Create your models here.

language = (
    ("uzbek","O'zbekcha"),
    ("russian","Ruscha"),
    ("english","Inglizcha"),
    ("turkish","Turkcha"),
    ("german","Nemischa"),
    ("others","Boshqa til")
)


class Category(models.Model):
    """  """
    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    """  """
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='authors_photo/', 
                              verbose_name="Rasm")
    about = models.TextField(verbose_name="Batafsil")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """  """
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.CharField(max_length=20, verbose_name="Til", choices=language, default="uzbek")
    about = models.TextField(verbose_name="Batafsil")
    publisher = models.CharField(max_length=50, verbose_name="Nashriyot")
    pages = models.PositiveIntegerField(verbose_name="Sahifalar soni")
    audio_file = models.FileField(upload_to='audios/', verbose_name="Audio")
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name="PDF")
    photo = models.ImageField(upload_to='books_photo/', verbose_name="Rasm")

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name





