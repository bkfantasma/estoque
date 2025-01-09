from django.contrib import admin
from .models import Fornecedores_loja

@admin.register(Fornecedores_loja)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'nome',
        'categoria'
    )
    search_fields= ('fornecedor',)
