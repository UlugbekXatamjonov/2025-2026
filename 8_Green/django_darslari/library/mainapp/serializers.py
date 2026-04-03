from rest_framework import serializers
from .models import Category, Author, Book


class Category_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]


class Author_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'photo', "about"]


class Book_Serializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    author_name = serializers.CharField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'name', 'language', 'about', "publisher",'pages','audio_file','pdf_file',
                  'photo','created_on','category_name', 'author_name']


class Category_Books_Serializers(serializers.ModelSerializer):
    books = Book_Serializers(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['id', 'name','books']
