from django.shortcuts import render, redirect, get_object_or_404
from projeto.fornecedores.models import Fornecedores_loja
from projeto.fornecedores.forms import FornecedorForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required 
def fornecedor(request):
    objects = Fornecedores_loja.objects.all()
    return render(request, "fornecedores_list.html", {"objects": objects})

@login_required 
def fornecedor_add(request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:fornecedor')
    else:
        form = FornecedorForm()
    
    return render(request, "fornecedor_form.html", {"form":form})

@login_required 
def fornecedor_edit(request, pk):
    fornecedor = get_object_or_404(Fornecedores_loja, pk=pk)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect("fornecedores:fornecedor")
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, "fornecedor_form.html", {"form": form})

def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedores_loja, pk=pk)
    fornecedor.delete()
    return redirect("fornecedores:fornecedor")

def fornecedores_json(request, pk):
    try:
        fornecedor = Fornecedores_loja.objects.get(pk=pk)
        data = {
            'id': fornecedor.id,
            'nome': fornecedor.nome,
        }
        return JsonResponse({'data': data})
    
    except Fornecedores_loja.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)
    
    except Exception as e:
        return JsonResponse({'error': f'Erro inesperado: {str(e)}'}, status=500)