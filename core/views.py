from django.shortcuts import render, get_object_or_404, redirect
from .models import Colaborador, Cliente, DireccionCliente, Producto
from .forms import ColaboradorForm, ClienteForm, DireccionClienteForm, ProductoForm

def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'core/colaborador_list.html', {'colaboradores': colaboradores})

def colaborador_create(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colaborador_list')
    else:
        form = ColaboradorForm()
    return render(request, 'core/colaborador_form.html', {'form': form})

def colaborador_update(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaborador_list')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'core/colaborador_form.html', {'form': form})

def colaborador_delete(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('colaborador_list')
    return render(request, 'core/colaborador_confirm_delete.html', {'object': colaborador})
# Create your views here.

def home (request):
    return render (request, 'core/home.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/cliente_lista.html', {'clientes': clientes})

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'core/cliente_form.html', {'form': form})

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'core/cliente_form.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'core/cliente_confirmar_eliminar.html', {'cliente': cliente})

def lista_direcciones(request):
    direcciones = DireccionCliente.objects.all()
    return render(request, 'core/direcciones_lista.html', {'direcciones': direcciones})

def crear_direccion(request):
    form = DireccionClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_direcciones')
    return render(request, 'core/direccion_form.html', {'form': form})

def actualizar_direccion(request, pk):
    direccion = get_object_or_404(DireccionCliente, pk=pk)
    form = DireccionClienteForm(request.POST or None, instance=direccion)
    if form.is_valid():
        form.save()
        return redirect('lista_direcciones')
    return render(request, 'core/direccion_form.html', {'form': form, 'direccion': direccion})

def eliminar_direccion(request, pk):
    direccion = get_object_or_404(DireccionCliente, pk=pk)
    if request.method == 'POST':
        direccion.delete()
        return redirect('lista_direcciones')
    return render(request, 'core/direccion_confirmar_eliminar.html', {'direccion': direccion})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/producto_lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'core/producto_form.html', {'form': form})

def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'core/producto_form.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'core/producto_confirmar_eliminar.html', {'producto': producto})

