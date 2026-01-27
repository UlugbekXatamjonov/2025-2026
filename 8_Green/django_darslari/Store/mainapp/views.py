from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

# Create your views here.
from .models import Category, Product
from .serializers import Category_Serializer, Product_Serializer


# ViewSets define the view behavior.
class Category_ViewSet(viewsets.ModelViewSet): # 
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    

class Product_ViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    
    
    
    
    
    
    
    