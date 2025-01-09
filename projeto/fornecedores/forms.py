from django import forms
from .models import Fornecedores_loja

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedores_loja
        fields = "__all__"