from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Cargo

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    nome = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    chave_acesso = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['nome', 'email', 'password1', 'chave_acesso', 'cargo']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
