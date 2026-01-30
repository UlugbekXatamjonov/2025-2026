from django.shortcuts import render
from rest_framework import viewsets

from .models import Category, Meal, Meal_type, QR_code
from .serializers import Category_List_Serializers, Category_Serializers, Meal_Serializer

# Create your views here.

class Category_List_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status='have')
    serializer_class = Category_List_Serializers


class Category_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status='have')
    serializer_class = Category_Serializers






