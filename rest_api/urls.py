from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_api.views import colaborador_list, colaborador_detail, producto_list, producto_detail
router = DefaultRouter()
router.register(r'colaboradores', colaborador_list, basename='colaborador')
router.register(r'productos', producto_list, basename='producto')

urlpatterns = [
    #path('', include(router.urls)),
    path('colaboradores/', colaborador_list),
    path('colaboradores/<int:pk>/', colaborador_detail),
    path('productos/', producto_list),
    path('productos/<int:pk>/', producto_detail),
]




