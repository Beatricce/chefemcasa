import os
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	return render(request,  'home.html' )

def buscar_chef(request):
	
	nome = request.POST['nome']
	chef_list = Chef.objects.filter(nome__contains=nome)
	return render(request, 'listar_chef.html', {'chef_list': chef_list})

def checkout(request):
	return render(request, 'checkout.html')

def filiacaoCliente(request):

	nome = request.POST['nome_cliente']
	sobrenome = request.POST['sobrenome_cliente']
	cpf = request.POST['CPF_cliente']
	endereco = request.POST['endereco_cliente']
	numero = request.POST['numero_cliente']
	complemento = request.POST['complemento_cliente']
	cidade = request.POST['cidade_cliente']
	estado = request.POST['estado_cliente']
	telefone = request.POST['telefone_cliente']
	cartao = request.POST['cartao_cliente']
	cartao_mm = request.POST['cartao_cliente_mm']
	cartao_yy = request.POST['cartao_cliente_yy']
	cartao_cvv = request.POST['cartao_cliente_cvv']

	return -1

def filiacaoChef(request):
	nome = request.POST['nome_chef']
	sobrenome = request.POST['sobrenome_chef']
	cpf = request.POST['CPF_chef']
	endereco = request.POST['endereco_chef']
	numero = request.POST['numero_chef']
	complemento = request.POST['complemento_chef']
	cidade = request.POST['cidade_chef']
	estado = request.POST['estado_chef']
	telefone = request.POST['telefone_chef']
	especialidades = request.POST['especialidade_chef']

	return -1