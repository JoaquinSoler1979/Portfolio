# serializers.py
from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'nombre', 'autor', 'fecha_publicacion']  # Incluye 'id' para identificarlo