from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Category_Serializers, Author_Serializers, Book_Serializers, Category_Books_Serializers, Author_Book_Serializers
from .models import Category, Author, Book


# Create your views here.

class Category_ViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = Category_Serializers

class Author_ViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.filter(status=True)
    serializer_class = Author_Serializers


class Book_ViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(status=True, language='uzbek')
    serializer_class = Book_Serializers
    
class Category_Books_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = Category_Books_Serializers

class Author_Book_Viewset(viewsets.ModelViewSet):
    queryset = Author.objects.filter(status=True)
    serializer_class = Author_Book_Serializers