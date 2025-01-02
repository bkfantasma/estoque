from django import forms
from .models import Estoque, EstoqueItens

class EstoqueForm(forms.ModelForm):

    class Meta:
        model = Estoque
        fields = ('funcionario', 'nf', 'movimento')
        widgets = {
            'movimento': forms.HiddenInput()
        }
        
class EstoqueItensForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('saldo')