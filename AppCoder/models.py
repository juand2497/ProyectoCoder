from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=40)
    direccion = models.CharField(max_length=80)
    
class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=40)
    apellido_empleado = models.CharField(max_length=40)
    puesto = models.CharField(max_length=30)
    salario = models.FloatField()
    
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    apellido_cliente = models.CharField(max_length=40)
    telefono = models.IntegerField()

class producto(models.Model):
    nombre_producto = models.CharField(max_length=40)
    valor = models.FloatField()
    fecha = models.DateField()
    entrega = models.BooleanField()
    
    
    