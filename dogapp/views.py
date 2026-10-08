from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
# Create your views here.

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer