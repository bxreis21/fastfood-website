from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.status}'

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
    detalhes = models.TextField()
    pago = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.cliente}'

# Create your models here.
