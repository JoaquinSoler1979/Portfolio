# landing/models.py
from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.IntegerField()