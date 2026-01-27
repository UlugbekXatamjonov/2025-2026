from rest_framework import serializers
from .models import Category, Product


class Category_Serializer(serializers.ModelSerializer): # Modelning qaysi maydonlari API bo'lishini belgilaydi
    class Meta:
        model = Category
        # fields = ('name', 'photo', 'status')
        fields = '__all__'

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'





