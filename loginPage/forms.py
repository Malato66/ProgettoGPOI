from django import forms
from .models import RispostaForm

class ModuloDatiForm(forms.ModelForm):
    class Meta:
        model = RispostaForm
        fields = ['nome_progetto', 'descrizione']