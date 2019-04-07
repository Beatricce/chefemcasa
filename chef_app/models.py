from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chef(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#primary_key=True,   !!!!!!!!!!
	nome = models.CharField ("Nome", max_length = 40)
	sobrenome = models.CharField("Sobrenome", max_length = 40)
	especialidades = models.TextField(null=True, blank=True)
	rg = models.IntegerField("RG", null=True, blank=True)
	cpf = models.IntegerField("CPF", null=True, blank=True)
	data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
	cep = models.IntegerField("CEP", null=True, blank=True)
	endereco_numero = models.IntegerField(null=True, blank=True) #endereco_rua sera pego automaticamente pelo cep
	celular = models.IntegerField(null=True, blank=True)
	nota = models.IntegerField(null=True, blank=True)
	foto = models.FileField(upload_to='fotos/', null=True, blank=True)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nome
		

class Cliente(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#primary_key=True,   !!!!!!!!!!
	nome = models.CharField("Nome", max_length = 40)
	sobrenome = models.CharField("Sobrenome", max_length = 40)
	rg = models.IntegerField("RG", null=True, blank=True)
	cpf = models.IntegerField("CPF", null=True, blank=True)
	data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
	cep = models.IntegerField("CEP", null=True, blank=True)
	endereco_numero = models.IntegerField(null=True, blank=True) #endereco_rua sera pego automaticamente pelo cep
	celular = models.IntegerField(null=True, blank=True)
	nota = models.IntegerField(null=True, blank=True)
	#agencia = models.IntegerField("Agencia", null=True, blank=True)
	#conta = models.IntegerField("Conta", null=True, blank=True)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nome
