from django.shortcuts import render, get_object_or_404, redirect
from .models import Colaborador, Cliente, DireccionCliente
from .forms import ColaboradorForm, ClienteForm, DireccionClienteForm

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
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'core/form_cliente.html', {'form': form})

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'core/form_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'core/confirmar_eliminar.html', {'cliente': cliente})

def lista_direcciones(request):
    direcciones = DireccionCliente.objects.all()
    return render(request, 'core/lista_direcciones.html', {'direcciones': direcciones})

def crear_direccion(request):
    form = DireccionClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_direcciones')
    return render(request, 'core/form_direccion.html', {'form': form})

def actualizar_direccion(request, pk):
    direccion = get_object_or_404(DireccionCliente, pk=pk)
    form = DireccionClienteForm(request.POST or None, instance=direccion)
    if form.is_valid():
        form.save()
        return redirect('lista_direcciones')
    return render(request, 'core/form_direccion.html', {'form': form, 'direccion': direccion})

def eliminar_direccion(request, pk):
    direccion = get_object_or_404(DireccionCliente, pk=pk)
    if request.method == 'POST':
        direccion.delete()
        return redirect('lista_direcciones')
    return render(request, 'core/confirmar_eliminar_direccion.html', {'direccion': direccion})

