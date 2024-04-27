from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .models import Colaborador, Cliente, DireccionCliente, Producto, Pedido, ProductoPedido
from .forms import ColaboradorForm, ClienteForm, DireccionClienteForm, ProductoForm, PedidoForm, ProductoPedidoForm, ProductoPedidoFormSet

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
    return render (request, 'core/home.html', {
        'title': 'Inicio'
    })

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

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'core/pedido_lista.html', {'pedidos': pedidos})

"""def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'core/pedido_form.html', {'form': form})"""

def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        formset = ProductoPedidoFormSet(request.POST, instance=pedido)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
        formset = ProductoPedidoFormSet(instance=pedido)  # Asegúrate de pasar la instancia aquí

    return render(request, 'core/pedido_form.html', {
        'form': form,
        'formset': formset
    })

def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'core/pedido_confirmar_eliminar.html', {'pedido': pedido})

def ver_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'core/pedido_ver.html', {'pedido': pedido})

"""def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        formset = ProductoPedidoFormSet(request.POST)
        if form.is_valid():
            pedido = form.save()
            formset = ProductoPedidoFormSet(request.POST)
            if formset.is_valid():
                formset.instance = pedido
                formset.save()
                return redirect('lista_pedidos')
    else:
        form = PedidoForm()
        formset = ProductoPedidoFormSet()
    return render(request, 'core/pedido_form.html', {
        'form': form,
        'formset': formset
    })"""

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'core/pedido_form.html', {'form': form})

def create_productopedido(request):
    if request.method == 'POST':
        form = ProductoPedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productopedido_list')
    else:
        form = ProductoPedidoForm()
    return render(request, 'core/productopedido_form.html', {'form': form})

def update_productopedido(request, pk):
    productopedido = ProductoPedido.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoPedidoForm(request.POST, instance=productopedido)
        if form.is_valid():
            form.save()
            return redirect('productopedido_list')
    else:
        form = ProductoPedidoForm(instance=productopedido)
    return render(request, 'core/productopedido_form.html', {'form': form})

def delete_productopedido(request, pk):
    ProductoPedido.objects.get(pk=pk).delete()
    return redirect('productopedido_list')

def list_productopedido(request):
    productopedidos = ProductoPedido.objects.all()
    return render(request, 'core/productopedido_list.html', {'productopedidos': productopedidos})