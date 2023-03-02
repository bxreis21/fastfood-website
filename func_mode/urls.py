from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.pedidos, name='pedidos'),
    path('cardapio_admin', views.cardapio_admin, name='cardapio_admin'),
    path('create_item', views.create_item, name='create_item'),
    path('edit_item/<int:item_id>', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    path('cancelar_pedido/<int:pedido_id>', views.cancelar_pedido, name='cancelar_pedido'),
    path('enviado_pedido/<int:pedido_id>', views.enviado_pedido, name='enviado_pedido'),
    path('tornar_pendente_pedido/<int:pedido_id>', views.tornar_pendente_pedido, name='tornar_pendente_pedido'),
]