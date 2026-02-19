from rest_framework import serializers
from .models  import New

# Serializers define the API representation.
class New_Serializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'



