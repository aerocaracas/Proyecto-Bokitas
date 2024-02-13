from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from bokitas.forms import SignUpForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'index.html')

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

@login_required  
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

