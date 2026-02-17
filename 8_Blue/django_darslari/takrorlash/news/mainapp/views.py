from django.shortcuts import render
from rest_framework import viewsets

from .models import New
from .serializers import New_Serizalizer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer