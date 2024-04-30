from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.conf import settings
from math import radians, cos, sin, asin, sqrt
from django.core.exceptions import ValidationError
import requests

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
    API_KEY = 'AIzaSyAEqGFaWx6amFhu-UJKZjfJn1UC2OMbDig'  # Replace this with your actual API key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': address, 'key': API_KEY}
    response = requests.get(base_url, params=params)
    response_data = response.json()
    
    if response_data['status'] == 'OK':
        latitude = response_data['results'][0]['geometry']['location']['lat']
        longitude = response_data['results'][0]['geometry']['location']['lng']
        print(latitude, longitude)
        return (latitude, longitude)
    else:
        return None

# Example usage:
#coords = get_coords("1600 Amphitheatre Parkway, Mountain View, CA")
#print(coords)



    

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

    def clean(self):
        super().clean()  # Ensure validation for other fields is also executed
        if self.direccion and self.tipo_entrega == 'delivery':
            delivery_coords = get_coords(self.direccion.direccion)
            if delivery_coords:
                main_lat = -33.018287658691406
                main_lon = -71.5504379272461
                distance = haversine(main_lon, main_lat, delivery_coords[1], delivery_coords[0])
                if distance > 5:
                    # Raise validation error if delivery is not possible
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