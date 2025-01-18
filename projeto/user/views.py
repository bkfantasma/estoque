from django.shortcuts import render, redirect
from projeto.user.models import User
from projeto.estoque.models import Estoque, EstoqueItens
from projeto.vendas.models import Venda
from projeto.user.forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Sum, Count


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password']) 
            user.save()
            return redirect('core:index')
    else:
        form = UserForm()
    return render(request, "cadastro.html", {"form": form})

def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                print("usuario logado!", user)
                return redirect('core:index')
            else:
                if user is None:
                    print(f"Autenticação falhou para email={email} e senha={password}")
                return render(request, 'signin.html', {
                    'form': form,
                    'error': 'email ou senha invalidos.'
                })
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form':form})

def logout(request):
    auth_logout(request)
    print('usuario deslogado!')
    return redirect("core:index")

@login_required
def user_dashboard(request):
    user = request.user  

    movimentacoes_estoque = Estoque.objects.filter(funcionario=user).order_by('-created')
    entradas_count = movimentacoes_estoque.filter(movimento='e').count()
    saidas_count = movimentacoes_estoque.filter(movimento='s').count()
    ultima_movimentacao = movimentacoes_estoque.aggregate(last_date=Max('created'))['last_date']

    vendas = Venda.objects.filter(user=user)

    total_vendido = vendas.aggregate(total=Sum('total'))['total'] or 0

    vendas_por_metodo = vendas.values('forma_pagamento').annotate(
        quantidade=Count('id'),
        total=Sum('total')
    )

    vendas_por_metodo_dict = {
        venda['forma_pagamento']: {
            'quantidade': venda['quantidade'],
            'total': venda['total']
        }
        for venda in vendas_por_metodo
    }

    context = {
        'user': user,
        'movimentacoes_estoque': movimentacoes_estoque,
        'entradas_count': entradas_count,
        'saidas_count': saidas_count,
        'ultima_movimentacao': ultima_movimentacao,
        'vendas': vendas,
        'total_vendido': total_vendido,
        'vendas_por_metodo': vendas_por_metodo_dict,
    }

    return render(request, 'dashboard.html', context)
