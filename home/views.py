from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    return render(request, 'home.html')

def register_page(request):
    if request.method != 'POST':
        print('erro')
        return render(request, 'register.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_conf = request.POST.get('senha2')

    print(nome, email, senha, senha_conf)

    if nome == '' or email == '' or senha == '' or senha_conf == '':
        messages.error(request, 'Por favor, insira todos os dados')
        print('entrou')
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

    user = User.objects.create_user(username=nome,email = email, password=senha)
    user.save()

    messages.success(request, 'Conta criada com sucesso')

    return render(request, 'login.html')

def login_page(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    user = request.POST['nome']
    senha = request.POST['senha']

    user = authenticate(username=user, password=senha)
  

    if user is not None:
        login(request, user)
        messages.success(request,'Logado com sucesso!')
        return redirect('index')

    else:
        messages.error(request, 'Não foi possível fazer login! Dados Incorretos, tente novamente.')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')



# Create your views here.
