from django.contrib import admin
from .models import Estoque, EstoqueItens, EstoqueEntrada, EstoqueSaida

class EstoqueItensInLine(admin.TabularInline):
    model = EstoqueItens
    extra = 0

@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInLine,)
    list_display=('__str__', 'nf')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'

@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInLine,)
    list_display=('__str__', 'nf')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
