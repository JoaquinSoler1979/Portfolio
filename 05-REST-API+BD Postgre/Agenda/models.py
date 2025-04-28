from django.db import models

# Create your models here.

class Agenda(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)