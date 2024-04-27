from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Colaborador, Cliente, DireccionCliente, Producto, Pedido, ProductoPedido])