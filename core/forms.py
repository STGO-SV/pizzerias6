from django import forms
from .models import Colaborador, Cliente, DireccionCliente, Producto, Pedido, ProductoPedido
from django.core import validators
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['rut', 'nombres', 'cargo']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']

class DireccionClienteForm(forms.ModelForm):
    class Meta:
        model = DireccionCliente
        fields = ['cliente', 'direccion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['tipo', 'nombre', 'precio']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccion', 'fecha', 'medio_pago', 'hora_pedido', 'horario_entrega', 'tipo_entrega']

class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['pedido', 'producto', 'cantidad']

ProductoPedidoFormSet = inlineformset_factory(
    Pedido, ProductoPedido,
    form=ProductoPedidoForm,
    fields=['producto', 'cantidad'],
    extra=1,
    can_delete=True
)