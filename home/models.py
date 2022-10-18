from django.db import models

class Accounts(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.EmailField()
    senha = models.CharField(max_length = 30)
    telefone = models.IntegerField(max_length=15)
    admin = models.BooleanField()


