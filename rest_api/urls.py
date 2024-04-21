from django.urls import path
from rest_api.views import colaborador_list, colaborador_detail

urlpatterns = [
    path('colaboradores/', colaborador_list),
    path('colaboradores/<int:pk>/', colaborador_detail),
]