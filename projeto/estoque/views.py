from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url, redirect
from .forms import EstoqueForm, EstoqueItensForm
from .models import Estoque, EstoqueItens
from django.contrib import messages

# Create your views here.

def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento = 'e')
    context = {'object_list': objects}
    return render(request, template_name, context)

def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    object = Estoque.objects.get(pk=pk)
    context = {'object': object}
    return render(request, template_name, context)

def estoque_entrada_add(request):
    estoque_form = Estoque()  
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,  
        min_num=1,  
        validate_min=True,
    )

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form)
        formset = item_estoque_formset(request.POST, instance=estoque_form)
        
        if form.is_valid() and formset.is_valid():
            estoque = form.save()  
            print(estoque)
            formset.instance = estoque
            
            formset.save() 
            messages.success(request, "Estoque e produtos adicionados com sucesso!")
            return redirect('estoque:estoque_entrada_detail', pk=estoque.pk)
        else:
            messages.error(request, "Erro ao adicionar o estoque ou produtos. Verifique os campos.")
    else:
        form = EstoqueForm(instance=estoque_form)
        formset = item_estoque_formset(instance=estoque_form)
   
    return render(request, 'estoque_entrada_form.html', {
        'form': form,
        'formset': formset,
    })