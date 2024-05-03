from django import forms
from .models import Colaborador, Cliente, DireccionCliente, Producto, Pedido, ProductoPedido
from django.core import validators
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import Colaborador

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['email'].label = 'Correo electrónico'
        self.fields['first_name'].label = 'Nombres'
        self.fields['last_name'].label = 'Apellidos'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Reingrese contraseña'

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class UserAdmin(BaseUserAdmin):
    form = UserAdminForm

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ColaboradorForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm password")

    class Meta:
        model = Colaborador
        fields = ['rut', 'nombres', 'cargo', 'username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password and confirm password does not match")

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        colaborador = super(ColaboradorForm, self).save(commit=False)
        colaborador.user = user
        if commit:
            colaborador.save()
        return colaborador

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