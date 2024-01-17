from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    DNI = models.CharField(max_length=100, default="DNI no establecido")
    metodo_pago = models.CharField(max_length=100, default="Metodo de pago no establecido")
    fecha_de_entrada = models.CharField(max_length=100, default="Fecha de entrada no establecida")
    numero_telefono = models.CharField(max_length=100, default= "Telefono no establecido")
