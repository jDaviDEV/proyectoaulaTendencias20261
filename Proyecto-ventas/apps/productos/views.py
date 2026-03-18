from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer
from apps.usuarios.permissions import EsVendedorOAdmin
 
 
class ProductoViewSet(viewsets.ModelViewSet):
 
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [EsVendedorOAdmin]