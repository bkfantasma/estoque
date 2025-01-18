from django import forms
from projeto.vendas.models import Venda, ItemVenda
from projeto.produto.models import Produto

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ('forma_pagamento', 'total')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'preco_unitario']
