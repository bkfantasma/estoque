from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import Produto, User, Cargo
from django.contrib.auth import authenticate

def home(request):
    produtos = Produto.objects.order_by('-id_produto')[:4]
    return render(request, 'index/home.html', {'produtos':produtos})

@login_required
def listagem_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos':produtos})

@login_required
def criar_produtos(request):
    if request.method == 'POST':
        new_product = Produto()
        new_product.nome = request.POST.get('nome') 
        new_product.categoria = request.POST.get('categoria')
        new_product.quantidade = request.POST.get('quantidade')
        new_product.preco = request.POST.get('preco')
        new_product.save()
        return redirect('home')
    return render(request, 'produtos/criar.html')

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
    return render(request, 'produtos/editar.html', {'produto': produto})

def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        user = authenticate(nome=nome, senha=senha)
        if user is not None:
            login(request, user)
            redirect('home')
        else:
            return render(request, 'user/login.html', {'error_message':'credenciais invalidas.'})

    return render(request, 'user/login.html')

def signup(request):
    return render(request, 'user/signup.html')

def criar_user(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    chave_acesso = request.POST.get('chave_acesso')
        
    if not (nome and email and senha and chave_acesso):
        return render(request, 'registration/signup.html', {'error_message': 'Todos os campos são obrigatórios.'})
        
    cargo = Cargo.objects.filter(nome='funcionario').first()
    if not cargo:
        return render(request, 'registration/signup.html', {'error_message': 'Cargo "funcionario" não encontrado.'})
        
    user = User(nome=nome, email=email, senha=senha, chave_acesso=chave_acesso, cargo=cargo)
    user.save()
        
    return redirect('login')