from rest_framework import serializers
from core.models import Colaborador, Cliente, DireccionCliente, Producto, Pedido, ProductoPedido    

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['rut', 'nombres', 'cargo']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']

class DireccionClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionCliente
        fields = ['cliente', 'direccion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['tipo', 'nombre', 'precio']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccion', 'fecha', 'medio_pago', 'hora_pedido', 'horario_entrega', 'tipo_entrega']

class ProductoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoPedido
        fields = ['pedido', 'producto', 'cantidad']