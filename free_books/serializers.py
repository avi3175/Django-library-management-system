from rest_framework import serializers
from .models import FreeBook

class FreeBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeBook
        fields = '__all__'
