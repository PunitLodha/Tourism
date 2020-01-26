from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
    places = serializers.JSONField(binary=True)
    hotels = serializers.JSONField(binary=True)
    class Meta:
        model = City
        fields = '__all__'