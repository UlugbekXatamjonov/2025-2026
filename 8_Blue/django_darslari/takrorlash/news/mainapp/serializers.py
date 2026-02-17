from rest_framework import serializers
from .models import New

class New_Serizalizer(serializers.ModelSerializer):
    class Meta:
        models = New
        fields = '__all__'    














