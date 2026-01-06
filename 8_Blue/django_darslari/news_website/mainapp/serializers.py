""" Serializer --> Modelning maydonlarini API ga o'tkazib beruvchi """

from rest_framework import serializers
from .models import News

class News_Serializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # fields = ['title','body', 'author', "image","video","views_count","read_time","tag","created_on","status",]




