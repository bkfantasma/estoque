from django.db import models

class Fornecedores_loja(models.Model):
    nome = models.CharField(max_length=100, null=False)
    categoria = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.nome