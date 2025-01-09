from django.shortcuts import render
from projeto.vendas.models import ItemVenda, Venda
from django.db.models import Sum

def index(request):
    produtos = ItemVenda.objects.values('produto__produto').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')

    produtos_nomes = [produto['produto__produto'] for produto in produtos]
    produtos_quantidade = [produto['total_vendido'] for produto in produtos]

    cores = ['#FF5733', '#33FF57', '#3357FF', '#F0FF33', '#FF33A1', '#33FFF7']
    
    produtos_data = [
        {
            'produto': nome,
            'quantidade_vendida': qtd,
            'cor': cores[i % len(cores)]
        }
        for i, (nome, qtd) in enumerate(zip(produtos_nomes, produtos_quantidade))
    ]

    context = {
        'produtos_nomes': produtos_nomes,
        'produtos_quantidade': produtos_quantidade,
        'produtos': produtos_data
    }
    return render(request, 'index.html', context)


def list_vendas(request):
    vendas = Venda.objects.all().order_by('-id')

    for venda in vendas:
        venda.total_calculado = 0 
        for item in venda.itens.all():
            item.subtotal = item.quantidade * item.preco_unitario
            venda.total_calculado += item.subtotal

    return render(request, 'list_vendas.html', {'vendas': vendas})
