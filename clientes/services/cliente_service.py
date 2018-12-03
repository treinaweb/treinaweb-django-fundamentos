from ..models import Cliente
from django.db import connection

def listar_clientes():
    clientes = Cliente.objects.all()
    return clientes

def listar_cliente_id(id):
    cliente = Cliente.objects.get(id=id)
    return cliente

def remover_cliente(cliente):
    cliente.delete()

def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, sexo=cliente.sexo, data_nascimento=cliente.data_nascimento,
                           email=cliente.email, profissao=cliente.profissao)

def editar_cliente(cliente, cliente_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE clientes_cliente SET nome={nome} WHERE id=2")
    cliente.nome = cliente_novo.nome
    cliente.sexo = cliente_novo.sexo
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.email = cliente_novo.email
    cliente.profissao = cliente_novo.profissao
    cliente.save(force_update=True)