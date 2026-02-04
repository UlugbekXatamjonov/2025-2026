from rest_framework import serializers
from .models import Category, Meal, Meal_type, QR_code


class Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'photo', 'description', 'price', 'weight')


class Category_List_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'photo')


class Category_Serializers(serializers.ModelSerializer):
    meals = Meal_Serializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'meals')




class Meal_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_type
        fields = ("name",  "price")


class Meal_detail_Serializer(serializers.ModelSerializer):
    types = Meal_type_Serializer(many=True, read_only=True)
    
    class Meta:
        model = Meal
        fields = ('id', 'name', 'photo', 'description', 'price', 'weight', 'types')




