from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm
from django.http import JsonResponse

def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)

def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    object = Produto.objects.get(pk=pk)
    context = {'object': object}
    return render(request, template_name, context)


def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

def produto_json(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        data = {
            'id': produto.id,
            'produto': produto.produto,
            'preco': produto.preco,
            'estoque': produto.estoque,
        }
        return JsonResponse({'data': data})
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)