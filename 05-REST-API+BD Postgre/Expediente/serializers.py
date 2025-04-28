from rest_framework import serializers
from .models import Expediente

class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediente
        fields = ['exp_id', 'organismo', 'numero', 'caratula', 'fechaultmov']