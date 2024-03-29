from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from bokitas.forms import SignUpForm, LoginForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'index.html')

# Registro de un nuevo usuario
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': SignUpForm
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
                    'form': SignUpForm,
                    "error": 'Usuario ya Existe!!!'
                })
        return render(request, 'signup.html', {
            'form': SignUpForm,
            "error": 'Password no Coincide'
        })

# Salir de la aplicacion
@login_required  
def signout(request):
    logout(request)
    return redirect('home')

# Iniciar Sesion
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': LoginForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': LoginForm,
                'error': 'Usuario o Password es Incorrecto'
            })
        else:
            login(request, user)
            return redirect('home')

