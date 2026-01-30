from rest_framework import serializers
from .models import Category, Meal, Meal_type, QR_code


class Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'category', 'photo', 'description', 'price', 'weight')


class Category_List_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'photo')


class Category_Serializers(serializers.ModelSerializer):
    meals = Meal_Serializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'meals')












