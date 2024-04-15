from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator

class Colaborador(models.Model):
    rut = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombres} - {self.cargo}"

# Crear un manager personalizado para el modelo de Cliente
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField(
        validators=[
            MaxValueValidator(999999999, message="Ingrese un número de hasta 9 dígitos sin letras o símbolos."),
            MinValueValidator(100000000, message="Ingrese un número de hasta 9 dígitos sin letras o símbolos.")
        ],
        error_messages={
            'required': "Este campo es obligatorio.",
            'invalid': "Ingrese un número válido."
        }
    )
    email = models.CharField(
        max_length=254, 
        unique=True,
        validators=[EmailValidator(message="Ingrese una dirección de correo válida.")]
    )

    def __str__(self):
        return f"{self.nombre} ({self.email})"
    
class DireccionCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.cliente.nombre} - {self.direccion}"

class Producto(models.Model):
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - ${self.precio}"

class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name='Cliente')
    direccion = models.ForeignKey('DireccionCliente', on_delete=models.SET_NULL, null=True, verbose_name='Dirección de entrega')
    fecha = models.DateField(default=timezone.now, verbose_name='Fecha del pedido')
    medio_pago = models.CharField(max_length=100, verbose_name='Medio de pago')
    hora_pedido = models.TimeField(default=timezone.localtime, verbose_name='Hora del pedido')
    horario_entrega = models.TimeField(verbose_name='Horario de entrega')
    tipo_entrega = models.CharField(max_length=50, verbose_name='Tipo entrega')

    def __str__(self):
        return f"{self.cliente.nombre} - {self.fecha}"

class ProductoPedido(models.Model):
    pedido = models.ForeignKey('Pedido', related_name='producto_pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.pedido} x {self.producto.nombre} x {self.cantidad}'