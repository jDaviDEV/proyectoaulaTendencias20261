from django.shortcuts import render
from rest_framework import viewsets
from .models import Cotizacion
from .serializer import CotizacionSerializer
from apps.usuarios.permissions import EsVendedorOAdmin
 
 
class CotizacionViewSet(viewsets.ModelViewSet):
 
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer
    permission_classes = [EsVendedorOAdmin]