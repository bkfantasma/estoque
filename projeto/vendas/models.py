from django.db import models
from projeto.produto.models import Produto
from projeto.user.models import User


class Venda(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=100, default='Dinheiro')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_total(self):
        self.total = sum(item.quantidade * item.preco_unitario for item in self.itens.all())
        self.save()

    def __str__(self):
        return f'Venda {self.id} - {self.data_venda}'


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens_venda', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} - Venda {self.venda.id}"
