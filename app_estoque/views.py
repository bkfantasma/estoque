from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, User, Cargo
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def home(request):
    produtos = Produto.objects.order_by('-id_produto')[:4]
    return render(request, 'app_estoque/index/home.html', {'produtos': produtos})

def listagem_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'app_estoque/produtos/produtos.html', {'produtos': produtos})

def criar_produtos(request):
    if request.method == 'POST':
        new_product = Produto()
        new_product.nome = request.POST.get('nome')
        new_product.categoria = request.POST.get('categoria')
        new_product.quantidade = request.POST.get('quantidade')
        new_product.preco = request.POST.get('preco')
        new_product.save()
        return redirect('home')
    return render(request, 'app_estoque/produtos/criar.html')

@login_required
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id_produto=produto_id)
    produto.delete()
    return redirect('listagem_produtos')

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id_produto=produto_id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.categoria = request.POST.get('categoria')
        produto.quantidade = request.POST.get('quantidade')
        produto.preco = request.POST.get('preco')
        produto.save()
        return redirect('listagem_produtos')
    return render(request, 'app_estoque/produtos/editar.html', {'produto': produto})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'app_estoque/registration/login.html', {'form': form})

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'app_estoque/registration/register.html', {'form': form})