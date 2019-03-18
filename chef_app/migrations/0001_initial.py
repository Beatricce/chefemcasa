# Generated by Django 2.1.4 on 2019-03-10 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=40, verbose_name='Sobrenome')),
                ('especialidades', models.TextField(blank=True, null=True)),
                ('rg', models.IntegerField(blank=True, null=True, verbose_name='RG')),
                ('cpf', models.IntegerField(blank=True, null=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('cep', models.IntegerField(blank=True, null=True, verbose_name='CEP')),
                ('endereco_numero', models.IntegerField(blank=True, null=True)),
                ('celular', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]