from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_clientes, name='listar_clientes'),
    path('cadastrar', inserir_cliente, name='cadastrar_cliente'),
    path('listar/<int:id>', listar_cliente_id, name='listar_cliente_id')
]