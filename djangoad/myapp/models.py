from django.db import models

# Create your models here.

class Members(models.Model):
    Primernombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255)

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)

class Cuentas(models.Model):
    nombre=models.CharField(max_length=30)


class Tarjetas(models.Model):
    numero=models.IntegerField()


class Prestamos(models.Model):
    nombre=models.CharField(max_length=30)


class Login(models.Model):
    nombre=models.CharField(max_length=30)