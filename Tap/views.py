from django.shortcuts import render
from rest_framework import generics
from .models import City
from .serializers import CitySerializer

class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
