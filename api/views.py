from django.shortcuts import render
from rest_framework import viewsets
from .serializer import InteraccionesSerializer
from .models import Interacciones
# Create your views here.
class InteraccioneViewSet(viewsets.ModelViewSet):
    queryset = Interacciones.objects.all()
    serializer_class = InteraccionesSerializer