from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField()
    categoria = models.TextField()
    quantidade = models.IntegerField()
    preco = models.IntegerField()

class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    permissao = models.IntegerField(null=True)

    def __str__(self):
        return self.nome

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    nome = models.CharField(max_length=100)
    chave_acesso = models.TextField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='usuarios')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=128, default='temp_password')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'senha', 'chave_acesso', 'cargo']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
