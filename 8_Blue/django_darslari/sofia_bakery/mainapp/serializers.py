
from rest_framework import serializers
from .models import Category, Cake, New


# Serializers define the API representation.
class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    cakes = CakeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'cakes')


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'

