from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Categoria, Carrinho, Item_Carrinho
from django.contrib.auth.decorators import login_required
from func_mode.models import Pedido,Status

def cardapio(request):
    itens = Item.objects.all().filter(disponivel_item=True)
    categorias = Categoria.objects.all()
    return render(request, 'cardapio.html', {'itens':itens , 'categorias': categorias})

@login_required(login_url='login')
def carrinho(request):  
    user = request.user
    carrinho = Carrinho.objects.get(user_carrinho=user) 
    itens_carrinho = Item_Carrinho.objects.filter(carrinho=carrinho)
    preco_total = 0
    for item in itens_carrinho:
        preco_total += item.item.preco_item * item.quantidade
        preco_total = round(preco_total, 2)

    return render(request, 'carrinho.html', {'itens': itens_carrinho, 'total': preco_total})

@login_required(login_url='login')
def item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        user = request.user
        quantidade = request.POST.get('quantidade')

        if not Carrinho.objects.filter(user_carrinho=user).exists():
            carrinho = Carrinho(user_carrinho=user)
            carrinho.save()
        
        else: 
            carrinho = Carrinho.objects.get(user_carrinho=user)
        
        for i in Item_Carrinho.objects.filter(carrinho=carrinho):
            if item == i.item:
                i.quantidade += int(quantidade)
                i.save()
                return redirect('cardapio')
     
        item_carrinho = Item_Carrinho(carrinho=carrinho, item=item, quantidade= quantidade)
        item_carrinho.save()
        return redirect('cardapio')
    return render(request, 'item.html', {'item': item })

@login_required(login_url='login')
def edit_carrinho(request, item_id):
    user = request.user
    carrinho = Carrinho.objects.get(user_carrinho=user) 
    deletado = Item.objects.get(id=item_id)
    Item_Carrinho.objects.filter(carrinho=carrinho, item=deletado).delete()
    return redirect('carrinho')

@login_required(login_url='login')
def enviar_pedido(request):
    user = request.user
    carrinho = Carrinho.objects.get(user_carrinho=user)
    itens_carrinho = Item_Carrinho.objects.filter(carrinho=carrinho)
    status = Status.objects.get(status='Pendente')

    detalhes_pedido = ''
    for item in itens_carrinho:
        nome_item = item.item.nome_item
        preco_item = item.item.preco_item
        quantidade_item = item.quantidade
        detalhes_pedido += f'<p>{nome_item} - {preco_item} x {quantidade_item}<p>'

    pedido = Pedido(cliente=user,detalhes=detalhes_pedido, status=status)
    pedido.save()
    Item_Carrinho.objects.filter(carrinho=carrinho).delete()

    return redirect('index')
 
