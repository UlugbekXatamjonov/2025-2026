from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Category_Serializers, Author_Serializers, Book_Serializers
from .models import Category, Author, Book


# Create your views here.

class Category_ViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializers

class Author_ViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = Author_Serializers


class Book_ViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book_Serializers
    
    