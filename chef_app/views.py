import os
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import admin
from django.http import HttpResponse

from .models import *
from datetime import datetime

# Create your views here.
def home(request):
	return render(request,  'home.html' )

def buscar_chef(request):
	
	nome = request.POST['nome']
	chef_list = Chef.objects.filter(nome__contains=nome)
	return render(request, 'listar_chef.html', {'chef_list': chef_list})

def checkout(request):
	return render(request, 'checkout.html')

def filiacaoChef(request):
	
	if request.method == 'POST':	

		nome = request.POST['nome_chef']
		sobrenome = request.POST['sobrenome_chef']
		especialidades = request.POST['especialidade_chef']
		print('especialidades: ',especialidades)
		rg = request.POST['rg_chef']
		rg = rg.replace(".","")
		rg = rg.replace("-","")
		cpf = request.POST['cpf_chef']
		cpf = cpf.replace(".","")
		cpf = cpf.replace("-","")
		user = User.objects.create_user(username=cpf, password='', email='')
		print("user: ", user)
		data_nascimento = request.POST['birthday_chef']
		data_nascimento = data_nascimento.replace("/","-")
		print("data: ",data_nascimento)
		ano = data_nascimento[6:8]
		ano_atual = datetime.now() 
		if int(ano) < (ano_atual.year)%100:
			ano = "19" + data_nascimento[6:8]
		else:
			ano = "20" + data_nascimento[6:8]
			#data_nascimento = data_nascimento.replace(data_nascimento[6:8],"19") + data_nascimento[6:8]
		data_nascimento = ano + "-" + data_nascimento[3:5] + "-" + data_nascimento[0:2]
		#print("data_nascimento:", data_nascimento)
		cep = request.POST['cep_chef']
		cep = cep.replace("-","")
		endereco_numero = request.POST['numero_chef']
		celular = request.POST['telefone_chef']
		celular = celular.replace("(","")
		celular = celular.replace(")","")
		celular = celular.replace("-","")
		foto = request.FILES['foto_chef']
		chef = Chef.objects.create(user=user, nome=nome, sobrenome=sobrenome, especialidades=especialidades, cpf=cpf, rg=rg, data_nascimento=data_nascimento, cep=cep, endereco_numero=endereco_numero, celular=celular, foto=foto)
		chef.save()

		#return HttpResponse("Welcome to the page at %s" % request.path)
		return render(request, 'checkout.html')

def filiacaoCliente(request):

	if request.method == 'POST':

		nome = request.POST['nome_cliente']
		sobrenome = request.POST['sobrenome_cliente']
		rg = request.POST['rg_cliente']
		rg = rg.replace(".","")
		rg = rg.replace("-","")
		cpf = request.POST['cpf_cliente']
		cpf = cpf.replace(".","")
		cpf = cpf.replace("-","")
		user = User.objects.create_user(username=cpf, password='', email='')
		print("user: ", user)
		data_nascimento = request.POST['birthday_cliente']
		data_nascimento = data_nascimento.replace("/","-")
		print("data: ",data_nascimento)
		ano = data_nascimento[6:8]
		ano_atual = datetime.now() 
		if int(ano) < (ano_atual.year)%100:
			ano = "19" + data_nascimento[6:8]
		else:
			ano = "20" + data_nascimento[6:8]
			#data_nascimento = data_nascimento.replace(data_nascimento[6:8],"19") + data_nascimento[6:8]
		data_nascimento = ano + "-" + data_nascimento[3:5] + "-" + data_nascimento[0:2]
		print("data_nascimento:", data_nascimento)
		cep = request.POST['cep_cliente']
		cep = cep.replace("-","")
		endereco_numero = request.POST['numero_cliente']
		celular = request.POST['telefone_cliente']
		celular = celular.replace("(","")
		celular = celular.replace(")","")
		celular = celular.replace("-","")
		#foto = request.POST['foto_cliente']
		cliente = Cliente.objects.create(user=user, nome=nome, sobrenome=sobrenome, cpf=cpf, rg=rg, data_nascimento=data_nascimento, cep=cep, endereco_numero=endereco_numero, celular=celular)
		cliente.save()
		
		#return HttpResponse("Welcome to the page at %s" % request.path)
		return render(request, 'checkout.html')
