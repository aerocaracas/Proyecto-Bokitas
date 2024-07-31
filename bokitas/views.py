from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from bokitas.forms import SignUpForm, LoginForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
                messages.success(request, "Cuenta creada Satisfactoriamente!!!")
                return redirect('home')
            except IntegrityError:
                messages.warning(request, "Usuario ya Existe!!!")
                return render(request, 'signup.html', {
                    'form': SignUpForm,
                })
        messages.warning(request, "Password no Coincide!!!")
        return render(request, 'signup.html', {
            'form': SignUpForm,
        })

# Salir de la aplicacion
@login_required  
def signout(request):
    logout(request)
    messages.success(request, "Cierre de sesión Satisfactoriamente!!!")
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
            messages.warning(request, "Usuario o Password es Incorrecto!!!")
            return render(request, 'signin.html', {
                'form': LoginForm,
            })
        else:
            login(request, user)
            messages.success(request, "Inicio de sesión Satisfactoriamente Bienvenido!!!")
            return redirect('home')

