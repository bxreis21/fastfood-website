from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from cardapio.models import Item


def index(request):
    itens = Item.objects.filter(vitrine=True)
    if request.user.is_authenticated:
        return render(request, 'home.html', {'permission':request.user.has_perm('pedidos.view_pedidos'), 'itens': itens})

    else:
        return render(request, 'home.html', {'itens': itens} )


def register_page(request):
    if request.user.is_authenticated:
        return render(request, 'register.html', {'permission':request.user.has_perm('pedidos.view_pedidos')})
        
    if request.method != 'POST':
        return render(request, 'register.html') 

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_conf = request.POST.get('senha2')

    if nome == '' or sobrenome == '' or email == '' or senha == '' or senha_conf == '':
        messages.error(request, 'Por favor, insira todos os dados')
        return render(request,'register.html')

    try:
        validate_email(email)

    except ValidationError:
        messages.error(request, "Por favor, insira um email válido.")
        return render(request, 'register.html')

    if User.objects.filter(username=nome).exists():
        messages.error(request, 'Nome de usuario já cadastrado em nosso site. Faça o login.')
        return render(request, 'register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado em nosso site. Faça o login.')
        return redirect('login')

    elif senha != senha_conf:
        messages.error(request,'As senhas não coincidem. Por favor, tente novamente.')
        return render(request, 'register.html')

    elif len(senha) < 6:
        messages.error(request, 'A senha deve ter no mínimo 6 caracteres')
        return render(request, 'register.html')

    user = User.objects.create_user(username= email, first_name=nome, last_name=sobrenome, email = email, password=senha)
    user.save()

    messages.success(request, 'Conta criada com sucesso')

    return render(request, 'login.html')

def login_page(request):
    if request.user.is_authenticated:
        return render(request, 'login.html', {'permission':request.user.has_perm('pedidos.view_pedidos')})

    if request.method != 'POST':
        return render(request, 'login.html')

    user = request.POST['nome']
    senha = request.POST['senha']

    user = authenticate(username=user, password=senha)
  
    if user is not None:
        login(request, user)
        return redirect('index')

    else:
        messages.error(request, 'Não foi possível fazer login! Dados Incorretos, tente novamente.')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

# Create your views here.
