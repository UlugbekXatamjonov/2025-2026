from django.shortcuts import render
from .serializers import CategorySerializer, CakeSerializer, NewSerializer
from .models import Category, Cake, New

from rest_framework import viewsets

# Create your views here.

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CakeViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.filter(status='have')
    serializer_class = CakeSerializer

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class Last_cakes_ViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.filter(status='have')[:1]
    serializer_class = CakeSerializer
