from django.shortcuts import render
from .models import New
from .serializers import New_Serializer
from rest_framework import viewsets
# Create your views here.


# ViewSets define the view behavior.
class New_ViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = New_Serializer
    
    