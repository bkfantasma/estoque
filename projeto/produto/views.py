from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)

@login_required 
def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    object = Produto.objects.get(pk=pk)
    context = {'object': object}
    return render(request, template_name, context)

@login_required 
def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)

class ProdutoCreate(LoginRequiredMixin, CreateView):  
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm
    login_url = '/user/signin/'  

class ProdutoUpdate(LoginRequiredMixin, UpdateView): 
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm
    login_url = '/user/signin/'

@login_required 
def produto_json(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        
        fornecedor_data = {
            'id': produto.fornecedor.id,
            'nome': produto.fornecedor.nome, 
        }

        data = {
            'id': produto.id,
            'produto': produto.produto,
            'preco': produto.preco,
            'estoque': produto.estoque,
            'fornecedor': fornecedor_data,
        }

        return JsonResponse({'data': data})
    
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    
    except Exception as e:
        return JsonResponse({'error': f'Erro inesperado: {str(e)}'}, status=500)

    

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)  
    produto.delete() 
    return redirect('produto:produto_list') 
