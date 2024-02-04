from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro de usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])     
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya Existe!!!'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password no Coincide'
        })
   
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Password es Incorrecto'
            })
        else:
            login(request, user)
            return redirect('home')
    
def proyecto(request):
    return render(request, 'proyecto.html')

def beneficiario(request):
    return render(request, 'beneficiario.html')

def medica(request):
    return render(request, 'medica.html')

def nutricional(request):
    return render(request, 'nutricional.html')

def socioeconomico(request):
    return render(request, 'socioeconomico.html')

def tareas(request):
    return render(request, 'tareas.html')


