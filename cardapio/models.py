from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'{self.nome_categoria}'
    
class Item(models.Model):
    nome_item = models.CharField(max_length=40)
    img = models.ImageField(upload_to="imagens_item", default='../media/default.jpg')
    preco_item = models.FloatField()
    valor_promocional = models.FloatField(default=0, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    ingredientes = models.TextField(blank=True, null=True)
    descricao = models.TextField()
    disponivel_item = models.BooleanField()
    vitrine = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.nome_item}'
    
class Carrinho(models.Model):
    user_carrinho = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_carrinho}'
    
class Item_Carrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.item.nome_item}'

class Combos(models.Model):
    nome_combo = models.CharField(max_length=40)
    preco_combo = models.CharField(max_length=40)
    itens_combo = models.ManyToManyField(Item)
    pessoas = models.SmallIntegerField()
    disponivel_item = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.nome_combo}'
    


# Create your models here.
