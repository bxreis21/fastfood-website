from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

def index(request):
    return render(request, 'home.html')

def register(request):
    if request.method != 'post':
        print('erro')
        return render(request, 'register.html')

    nome = request.POST.get(name='nome')
    email = request.POST.get(name='email')
    senha = request.POST.get(name='senha')
    telefone = request.POST.get(name='telefone')

    user = User.objects.create_user(username=nome,email = email, password=senha)
    user.telefone = telefone
    user.save()

    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
# Create your views here.
