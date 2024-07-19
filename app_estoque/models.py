from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField()
    categoria = models.TextField()
    quantidade = models.IntegerField()
    preco = models.FloatField(float)

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    permissao = models.IntegerField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    email = models.EmailField()
    senha = models.TextField()
    chave_acesso = models.TextField()    
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='usuarios')
    