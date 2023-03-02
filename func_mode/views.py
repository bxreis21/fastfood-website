from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Status
from django.contrib.auth.decorators import permission_required
from cardapio.models import Item, Categoria
from django.contrib import messages

@permission_required('pedidos.can_view_pedidos', login_url='/login')
def pedidos(request):
    pedidos = Pedido.objects.all()
    status = Status.objects.all()
    return render(request, 'pedidos.html', {'pedidos':pedidos, 'status': status})

@permission_required('cardapio.can_change_item', login_url='/login')
def cardapio_admin(request):
    itens = Item.objects.all().filter()
    categorias = Categoria.objects.all()
    return render(request, 'cardapio_admin.html', {'itens': itens, 'categorias': categorias})

@permission_required('cardapio.can_change_item', login_url='/login')
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        edits = {
            'nome':request.POST.get('nome'), 
            'img': item.img if request.FILES.get('img') is None else request.FILES.get('img'), 
            'preco':request.POST.get('preco'),
            'valor_promocional':request.POST.get('valor_promocional'),
            'categoria':Categoria.objects.get(nome_categoria=request.POST.get('categoria')),
            'ingredientes':request.POST.get('ingredientes'),
            'descricao':request.POST.get('descricao'),
            'disponivel':request.POST.get('disponivel'),
            'vitrine': request.POST.get('vitrine'),
            }
        
        item = Item(
            id = item_id,
            nome_item = edits['nome'],
            img = edits['img'],
            preco_item = edits['preco'],
            valor_promocional = edits['valor_promocional'],
            categoria = edits['categoria'],
            ingredientes = edits['ingredientes'],
            descricao = edits['descricao'],
            disponivel_item = True if edits['disponivel'] else False,    
            vitrine = True if edits['vitrine'] else False,
            )

        messages.success(request, 'Item editado com sucesso')
        item.save()
    
    return render(request, 'edit_item.html', {'item': item, 'categorias': categorias})

@permission_required('cardapio.can_delete_item', login_url='/login')
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('cardapio_admin')

@permission_required('cardapio.can_add_item', login_url='/login')
def create_item(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        edits = {
            'nome':request.POST.get('nome'), 
            'img': request.FILES.get('img'),
            'preco':request.POST.get('preco'),
            'valor_promocional':request.POST.get('valor_promocional') if request.POST.get('valor_promocional') != '' else 0,
            'categoria': request.POST.get('categoria'),
            'ingredientes':request.POST.get('ingredientes'),
            'descricao':request.POST.get('descricao'),
            'disponivel':request.POST.get('disponivel'),
            }
        
        print(edits['img'])
        
        if edits['nome'] == '' or edits['preco'] == '' or edits['categoria'] == '' or edits['descricao']== '' :
            messages.error(request, 'Por Favor, insira todas as informações obrigatórias')
            return render(request,'create_item.html', {'categorias': categorias})

        else:
            categoria = Categoria.objects.get(nome_categoria=edits['categoria'])
            disponivel = True if edits['disponivel'] else False
            item = Item(
                nome_item = edits['nome'],
                img = edits['img'],
                preco_item = edits['preco'],
                valor_promocional = edits['valor_promocional'],
                categoria = categoria,
                ingredientes = edits['ingredientes'],
                descricao = edits['descricao'],
                disponivel_item = disponivel,
                )

            item.save()
            return redirect('cardapio_admin')
    
    return render(request, 'create_item.html', {'categorias': categorias})


@permission_required('pedidos.can_edit_item', login_url='/login')
def cancelar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido,id=pedido_id)
    status = Status.objects.get(status='Cancelado')
    pedido = Pedido(
        id=pedido_id, 
        cliente=pedido.cliente, 
        data=pedido.data, 
        detalhes=pedido.detalhes, 
        pago=pedido.pago, 
        status=status )
    pedido.save()
    return redirect('pedidos')

@permission_required('pedidos.can_add_item', login_url='/login')
def enviado_pedido(request, pedido_id):
    print(pedido_id)
    pedido = get_object_or_404(Pedido,id=pedido_id)
    status = Status.objects.get(status='Enviado')
    pedido = Pedido(
        id=pedido_id, 
        cliente=pedido.cliente, 
        data=pedido.data, 
        detalhes=pedido.detalhes, 
        pago=pedido.pago, 
        status=status )
    pedido.save()
    return redirect('pedidos')

@permission_required('pedidos.can_add_item', login_url='/login')
def tornar_pendente_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido,id=pedido_id)
    status = Status.objects.get(status='Pendente')
    pedido = Pedido(
        id=pedido_id, 
        cliente=pedido.cliente, 
        data=pedido.data, 
        detalhes=pedido.detalhes, 
        pago=pedido.pago, 
        status=status )
    pedido.save()
    return redirect('pedidos')



