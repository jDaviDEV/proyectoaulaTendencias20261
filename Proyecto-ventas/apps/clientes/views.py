from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializer import ClienteSerializer
from apps.usuarios.permissions import EsVendedorOAdmin
 
 
class ClienteViewSet(viewsets.ModelViewSet):
 
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [EsVendedorOAdmin]