
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('colaboradores/', views.colaborador_list, name='colaborador_list'),
    path('colaboradores/new', views.colaborador_create, name='colaborador_create'),
    path('colaboradores/<int:pk>/edit/', views.colaborador_update, name='colaborador_update'),
    path('colaboradores/<int:pk>/delete/', views.colaborador_delete, name='colaborador_delete'),
     path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('clientes/<int:pk>/editar/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('direcciones/', views.lista_direcciones, name='lista_direcciones'),
    path('direcciones/nuevo/', views.crear_direccion, name='crear_direccion'),
    path('direcciones/<int:pk>/editar/', views.actualizar_direccion, name='actualizar_direccion'),
    path('direcciones/<int:pk>/eliminar/', views.eliminar_direccion, name='eliminar_direccion'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/editar/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/nuevo/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/<int:pk>/editar/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/<int:pk>/eliminar/', views.eliminar_pedido, name='eliminar_pedido'),

]