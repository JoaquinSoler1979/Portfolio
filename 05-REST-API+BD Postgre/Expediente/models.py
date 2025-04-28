from django.db import models

# Create your models here.

class Expediente(models.Model):
    exp_id = models.CharField(max_length=150)
    organismo = models.CharField(max_length=80)
    numero = models.CharField(max_length=20)
    caratula = models.CharField(max_length=150)
    fechaultmov = models.CharField(max_length=150)