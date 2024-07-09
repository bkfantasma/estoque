from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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

class UserManager(BaseUserManager):
    def create_user(self, email, nome, chave_acesso, cargo, password=None):
        if not email:
            raise ValueError('O usuário deve ter um endereço de email')
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            chave_acesso=chave_acesso,
            cargo=cargo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, chave_acesso, cargo, password=None):
        user = self.create_user(
            email=email,
            nome=nome,
            chave_acesso=chave_acesso,
            cargo=cargo,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    nome = models.CharField(max_length=100)
    chave_acesso = models.TextField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='usuarios')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    senha = models.CharField(max_length=128, default='temp_password')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'chave_acesso', 'cargo']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin