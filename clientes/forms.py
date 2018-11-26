from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'data_nascimento', 'email', 'profissao']