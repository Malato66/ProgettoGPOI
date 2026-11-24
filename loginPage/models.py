from django.db import models
from django.contrib.auth.models import User

class RispostaForm(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE) # collega la risposta a chi ha fatto login
    nome_progetto = models.CharField(max_length=100)
    descrizione = models.TextField()
    data_invio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_progetto} - {self.utente.username}"