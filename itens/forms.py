from django import forms 
from .models import Itens

class NewItensForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = ['nome', 'tipo', 'descricao', 'contato', 'foto']