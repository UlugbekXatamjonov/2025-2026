from rest_framework import serializers
from .models import Category, Author, Book


class Category_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'status']


class Author_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'photo', "about", 'status']


class Book_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


