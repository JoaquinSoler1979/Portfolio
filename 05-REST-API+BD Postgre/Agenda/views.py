from rest_framework import viewsets
from .models import Agenda
from .serializers import AgendaSerializer

class AgendaViewSet(viewsets.ModelViewSet): 
    queryset = Agenda.objects.all()  # Obtiene todos los libros
    serializer_class = AgendaSerializer  # Usa el serializador creado


