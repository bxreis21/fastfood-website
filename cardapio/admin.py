from django.contrib import admin
from .models import Categoria, Item, Carrinho, Item_Carrinho

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome_categoria']
    list_display_links = ['nome_categoria']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','nome_item', 'preco_item','categoria', 'disponivel_item']
    list_display_link = ['nome_item']
    list_editable = ['disponivel_item']

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['id','user_carrinho']
    list_display_links = ['id', 'user_carrinho']

class Item_CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['carrinho', 'item', 'quantidade']
    list_display_link = ['carrinho']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Item, ItemAdmin)
# admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(Item_Carrinho, Item_CarrinhoAdmin)

# Register your models here.
