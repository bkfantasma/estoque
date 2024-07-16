from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    categoria = models.TextField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.FloatField(float)

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    permissao = models.IntegerField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    senha = models.TextField(max_length=255)
    chave_acesso = models.TextField(max_length=3)    
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='usuarios')
    