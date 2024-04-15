from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Colaborador(models.Model):
    rut = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.nombres} - {self.cargo}"

# Crear un manager personalizado para el modelo de Cliente
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"
    
class DireccionCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    
    def _str_(self):
        return f"{self.cliente.nombre} - {self.direccion}"

class Producto(models.Model):
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.nombre} ({self.tipo}) - ${self.precio}"

