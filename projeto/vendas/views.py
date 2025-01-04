from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Venda, ItemVenda
from .forms import VendaForm, ItemVendaForm
from django.contrib.auth.decorators import login_required

@login_required
def register_venda(request):
    ItemVendaFormSet = modelformset_factory(
        ItemVenda,
        form=ItemVendaForm,
        fields=('produto', 'quantidade', 'preco_unitario'),
        extra=0,
        min_num=0,
    )

    if request.method == 'POST':
        venda_form = VendaForm(request.POST)
        item_venda_formset = ItemVendaFormSet(request.POST, prefix='estoques')

        if venda_form.is_valid() and item_venda_formset.is_valid():
            venda = venda_form.save(commit=False)
            venda.save()  

            for form in item_venda_formset:
                item_venda = form.save(commit=False)
                item_venda.venda = venda 
                item_venda.save()

                produto = item_venda.produto
                quantidade_vendida = item_venda.quantidade

                if produto.estoque >= quantidade_vendida:
                    produto.estoque -= quantidade_vendida
                    produto.save()
                else:
                    messages.error(request, f"Estoque insuficiente para o produto {produto.produto}.")
                    return redirect('vendas:register_venda')

            venda.calcular_total()

            return redirect('vendas:gerar_recibo', venda_id=venda.id)
    else:
        venda_form = VendaForm()
        item_venda_formset = ItemVendaFormSet(queryset=ItemVenda.objects.none(), prefix='estoques')

    return render(request, 'register_venda_form.html', {
        'venda_form': venda_form,
        'item_venda_formset': item_venda_formset,
    })

def gerar_recibo(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    itens = venda.itens.all()  
    total = sum([item.quantidade * item.preco_unitario for item in itens])

    return render(request, 'gerar_recibo.html', {
        'venda': venda,
        'itens': itens,
        'total': total,
    })
