from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def home(request):
    produtos = Produto.objects.order_by('-id_produto')[:4]

    return render(request, 'index/home.html', {'produtos':produtos})

def listagem_produtos(request):
    produtos = Produto.objects.all()
    
    return render(request, 'produtos/produtos.html', {'produtos':produtos})

def criar_produtos(request):
    # Cria produto novo 

    new_product = Produto()
    new_product.nome = request.POST.get('nome') 
    new_product.categoria = request.POST.get('categoria')
    new_product.quantidade = request.POST.get('quantidade')
    new_product.preco = request.POST.get('preco')
    new_product.save()

    return redirect(home)

def deletar_produto(request, produto_id):
    # Deletar produto

    produto = get_object_or_404(Produto, id_produto=produto_id)
    produto.delete()

    return redirect(listagem_produtos)

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