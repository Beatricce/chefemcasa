# Generated by Django 2.1.5 on 2019-04-08 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef_app', '0003_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='conta',
        ),
    ]
