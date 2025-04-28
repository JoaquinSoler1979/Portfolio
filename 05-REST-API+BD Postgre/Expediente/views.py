from rest_framework import viewsets
from .models import Expediente
from .serializers import ExpedienteSerializer
import FachadaPersistencia as fp

class ExpedienteViewSet(viewsets.ModelViewSet):

    serializer_class = ExpedienteSerializer
    fp.actualizarDB()
    queryset = Expediente.objects.all()

    