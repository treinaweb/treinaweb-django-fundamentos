from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_clientes, name='listar_clientes')
]