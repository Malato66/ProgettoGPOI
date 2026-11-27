from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ModuloDatiForm
from .forms import RegistrazioneForm

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Crea la sessione per l'utente
            return redirect('index')
            
    return render(request, 'login.html')

def registrazione(request):
    if request.method == 'POST':
        form = RegistrazioneForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Sostituisci 'index' con il name della tua home in urls.py
    else:
        form = RegistrazioneForm()
        
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
