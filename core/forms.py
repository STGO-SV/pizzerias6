from django import forms
from .models import Colaborador, Cliente, DireccionCliente, Producto

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