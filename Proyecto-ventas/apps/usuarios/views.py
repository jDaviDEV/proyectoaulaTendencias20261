from rest_framework import viewsets
from .models import Usuario
from .serializer import UsuarioSerializer
from .permissions import EsAdministrador
 
 
class UsuarioViewSet(viewsets.ModelViewSet):
 
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
 
   
    permission_classes = [EsAdministrador]