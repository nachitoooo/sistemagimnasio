from django.db import models
from datetime import timedelta

class User(models.Model):
    DNI = models.CharField(max_length=100, default="DNI no establecido")
    metodo_pago = models.CharField(max_length=100, default="Metodo de pago no establecido")
    fecha_de_entrada = models.DateField(default="0-0-0")
    numero_telefono = models.CharField(max_length=100, default="Telefono no establecido")
    dias_abonados = models.IntegerField(default=0)
