from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def inserir_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})

def listar_cliente_id(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})
