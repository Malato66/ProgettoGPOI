from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ModuloDatiForm

def index(request):
    return render(request, 'index.html')

def registrazione(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            utente = form.save()
            login(request, utente)
            return redirect('compila_modulo')
    else:
        form = UserCreationForm()

    return render(request, 'registrazione.html', {'form': form})

@login_required
def compila_modulo(request):
    if request.method == 'POST':
        form = ModuloDatiForm(request.POST)
        if form.is_valid():
            risposta = form.save(commit=False)
            risposta.utente = request.user
            risposta.save()
            return render(request, 'conferma.html')
    else:
        form = ModuloDatiForm()

    return render(request, 'modulo.html', {'form': form})
