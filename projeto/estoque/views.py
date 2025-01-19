import json
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import EstoqueForm, EstoqueItensForm
from .models import Estoque, EstoqueItens, EstoqueEntrada, EstoqueSaida
from projeto.produto.models import Produto
from django.http import JsonResponse

User = get_user_model()

@login_required 
def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = EstoqueEntrada.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_name, context)

@login_required 
def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    object = EstoqueEntrada.objects.get(pk=pk)
    if object != None:
        context = {'object': object}
        return render(request, template_name, context)
    return redirect("core:index")

def dar_baixa_estoque_add(estoque):
    produtos = estoque.estoques.all()
    if produtos.exists():
        for item in produtos:
            produto = Produto.objects.get(pk=item.produto.pk)
            produto.estoque += item.quantidade
            produto.save()
            print('estoque atualizado!')
    else:
        print("Nenhum produto encontrado para o estoque.")

def dar_baixa_estoque_saida(estoque):
    produtos = estoque.estoques.all()
    if produtos.exists():
        for item in produtos:
            produto = Produto.objects.get(pk=item.produto.pk)
            produto.estoque -= item.quantidade
            produto.save()
            print('estoque atualizado!')
    else:
        print("Nenhum produto encontrado para o estoque.")

@login_required
def estoque_entrada_add(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    estoque_form = EstoqueEntrada()
    print("Funcionário:", request.user)
    item_estoque_formset = inlineformset_factory(
        EstoqueEntrada,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=0,
        validate_min=True,
        can_delete=False,
    )

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form)
        formset = item_estoque_formset(request.POST, instance=estoque_form)

        if form.is_valid() and formset.is_valid():
            estoque = form.save(commit=False)
            estoque.funcionario = request.user
            estoque.movimento = 'e'
            estoque.save()
            formset.instance = estoque
            formset.save()
            dar_baixa_estoque_add(estoque)
            return redirect('estoque:estoque_entrada_detail', pk=estoque.pk)
    else:
        form = EstoqueForm(instance=estoque_form)
        form.fields['movimento'].initial = 'e'
        formset = item_estoque_formset(instance=estoque_form)

    return render(request, 'estoque_entrada_form.html', {
        'form': form,
        'formset': formset,
    })

@login_required 
def estoque_saida_list(request):
    template_name = 'estoque_saida_list.html'
    objects = EstoqueSaida.objects.filter(movimento='s')
    context = {'object_list': objects}
    return render(request, template_name, context)

@login_required
def estoque_saida_add(request):
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=0,
        validate_min=True,
        can_delete=False,
    )

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form)
        formset = item_estoque_formset(request.POST, instance=estoque_form)

        if form.is_valid() and formset.is_valid():
            estoque = form.save(commit=False)
            estoque.funcionario = request.user
            estoque.movimento = 's'
            estoque.save()
            formset.instance = estoque
            formset.save()
            dar_baixa_estoque_saida(estoque)
            return redirect('estoque:estoque_saida_detail', pk=estoque.pk)

    else:
        form = EstoqueForm(instance=estoque_form)
        form.fields['movimento'].initial = 's'
        formset = item_estoque_formset(instance=estoque_form)

    return render(request, 'estoque_saida_form.html', {
        'form': form,
        'formset': formset,
    })

@login_required 
def estoque_saida_detail(request, pk):
    template_name = 'estoque_saida_detail.html'
    object = EstoqueSaida.objects.get(pk=pk)
    if object != None:
        context = {'object': object}
        return render(request, template_name, context)
    return redirect("core:index")
