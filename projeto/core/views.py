from django.shortcuts import render
from projeto.vendas.models import Venda

def index(request):
    return render(request, "index.html")

def list_vendas(request):
    vendas = Venda.objects.all()

    for venda in vendas:
        venda.total_calculado = 0 
        for item in venda.itens.all():
            item.subtotal = item.quantidade * item.preco_unitario
            venda.total_calculado += item.subtotal

    return render(request, 'list_vendas.html', {'vendas': vendas})
