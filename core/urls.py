
from django.urls import path
from .views import home
from . import views
urlpatterns = [
    path('', home, name="home"),
    path('colaboradores/', views.colaborador_list, name='colaborador_list'),
    path('colaboradores/new', views.colaborador_create, name='colaborador_create'),
    path('colaboradores/<int:pk>/edit/', views.colaborador_update, name='colaborador_update'),
    path('colaboradores/<int:pk>/delete/', views.colaborador_delete, name='colaborador_delete'),

]