from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def inserir_cliente(request):
    form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})
