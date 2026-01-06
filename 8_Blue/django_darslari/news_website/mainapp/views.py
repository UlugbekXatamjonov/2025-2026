from django.shortcuts import render
from .models import News
from .serializers import News_Serializer

from rest_framework import viewsets

# Create your views here.


class News_ViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = News_Serializer



