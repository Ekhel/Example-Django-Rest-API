from django.shortcuts import render
from rest_framework import viewsets
from .models import Nelayan
from .serializers import NelayanSerializers

class NelayanView(viewsets.ModelViewSet):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializers
