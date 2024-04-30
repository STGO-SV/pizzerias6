from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_api.views import colaborador_list, colaborador_detail
router = DefaultRouter()
router.register(r'colaboradores', colaborador_list, basename='colaborador')

urlpatterns = [
    #path('', include(router.urls)),
    path('colaboradores/', colaborador_list),
    path('colaboradores/<int:pk>/', colaborador_detail),
]




