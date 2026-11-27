from django import forms
from .models import RispostaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ModuloDatiForm(forms.ModelForm):
    class Meta:
        model = RispostaForm
        fields = ['nome_progetto', 'descrizione']

class RegistrazioneForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Cognome")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')