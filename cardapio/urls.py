from django.urls import path
from . import views 

urlpatterns = [
    path('', views.cardapio, name='cardapio'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('<int:item_id>', views.item, name='item'),
    path('deteted_<int:item_id>', views.edit_carrinho, name='edit_carrinho'),
    path('enviar_pedido', views.enviar_pedido, name='enviar_pedido'),
]

