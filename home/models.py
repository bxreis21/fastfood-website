from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length = 50)
    telefone = models.IntegerField()
    admin = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.nome}'

class Endereco(models.Model):
    conta = models.ForeignKey(Account, on_delete=models.CASCADE)
    rua = models.CharField(max_length=70)
    num = models.IntegerField()
    cep = models.CharField(max_length=8)
    ref = models.TextField()
    bairro = models.CharField(max_length=25)
    estado = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
