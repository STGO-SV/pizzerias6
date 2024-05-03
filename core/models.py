from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.conf import settings
from math import radians, cos, sin, asin, sqrt
from django.core.exceptions import ValidationError
import requests
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

'''<!DOCTYPE html>
<html>
  <head>
    <title>Simple Marker</title>
    <!-- The callback parameter is required, so we use console.debug as a noop -->
    <script async src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY_HERE&callback=console.debug&libraries=maps,marker&v=beta">
    </script>
    <link rel="stylesheet" href="./style.css"/>
  </head>
  <body>
    <gmp-map center="-33.018287658691406,-71.5504379272461" zoom="14" map-id="DEMO_MAP_ID">
      <gmp-advanced-marker position="-33.018287658691406,-71.5504379272461" title="My location"></gmp-advanced-marker>
    </gmp-map>
  </body>
</html>'''


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees).
    """
    # Convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(max(0, min(1, a))))  # Safeguard against precision issues
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371.0
    return c * r






def get_coords(address):
    API_KEY = 'AIzaSyAEqGFaWx6amFhu-UJKZjfJn1UC2OMbDig'
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': address, 'key': API_KEY}
    response = requests.get(base_url, params=params)
    response_data = response.json()
    if response_data['status'] == 'OK':
        for result in response_data['results']:
            if "street_address" in result['types'] or "premise" in result['types']:
                latitude = result['geometry']['location']['lat']
                longitude = result['geometry']['location']['lng']
                print(latitude, longitude)
                return (latitude, longitude)
            raise ValidationError("La dirección no es clara.")
    else:
        raise ValidationError("No se puede validar la dirección.")

class Colaborador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='colaborador')
    CARGO_CHOICES = [
        ('Driver', 'Driver'),
        ('Operario', 'Operario'),
        ('Jefe de turno', 'Jefe de turno'),
        ('Gerente', 'Gerente'),
    ]
    rut = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)

    class Meta:
        permissions = [
            ('agregar_pedido', 'Puede agregar pedido'),
            ('ver_detalles', 'Puede ver detalles'),
            ('editar_pedido', 'Puede editar pedido'),
            ('eliminar_pedido', 'Puede eliminar pedido'),
        ]

    def __str__(self):
        return f"{self.nombres} - {self.cargo}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # En etapa de prueba
        group = Group.objects.get(name='Colaboradores')
        if self.cargo in ['Operario', 'Driver']:
            group.user_set.add(self.usuario)  # En etapa de prueba
        else:
            group.user_set.remove(self.usuario)
        group.save()

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
    TIPO_ENTREGA_CHOICES = (
        ('delivery', 'Delivery'),
        ('retiro', 'Retiro en tienda'),
        ('consumo', 'Consumo en local'),
    )
    MEDIO_PAGO_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('mercadopago', 'Mercadopago'),
        ('sodexo', 'Sodexo'),
    )
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name='Cliente')
    direccion = models.ForeignKey('DireccionCliente', on_delete=models.SET_NULL, null=True, verbose_name='Dirección de entrega')
    fecha = models.DateField(default=timezone.now, verbose_name='Fecha del pedido')
    medio_pago = models.CharField(max_length=100, choices=MEDIO_PAGO_CHOICES, verbose_name='Medio de pago')
    hora_pedido = models.TimeField(default=timezone.localtime, verbose_name='Hora del pedido')
    horario_entrega = models.TimeField(verbose_name='Horario de entrega')
    tipo_entrega = models.CharField(max_length=50, choices=TIPO_ENTREGA_CHOICES, verbose_name='Tipo entrega')

    def clean(self):
        super().clean()  # Ensure validation for other fields is also executed
        if self.direccion and self.tipo_entrega == 'delivery':
            delivery_coords = get_coords(self.direccion.direccion)
            if delivery_coords:
                main_lat = -33.018287658691406
                main_lon = -71.5504379272461
                distance = haversine(main_lon, main_lat, delivery_coords[1], delivery_coords[0])
                if distance > 5:
                    # Presentar error si distancia es mayor
                    raise ValidationError("No puede hacerse delivery, dirección lejana. Por favor cambie el tipo de entrega.")
            else:
                raise ValidationError("No se pudo determinar las coordenadas de la dirección de entrega.")

    def _str_(self):
        return f"{self.cliente.nombre} - {self.fecha}"

class ProductoPedido(models.Model):
    pedido = models.ForeignKey('Pedido', related_name='producto_pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.pedido} x {self.producto.nombre} x {self.cantidad}'