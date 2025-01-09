from django.contrib import admin
from .models import Venda

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'data_venda',
        'forma_pagamento',
        'total',
    )
    search_fields = ('forma_pagamento',)