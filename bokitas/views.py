from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TareaForm
from .models import Tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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

@login_required      
def proyecto(request):
    return render(request, 'proyecto.html')

@login_required  
def beneficiario(request):
    return render(request, 'beneficiario.html')

@login_required  
def medica(request):
    return render(request, 'medica.html')

@login_required  
def nutricional(request):
    return render(request, 'nutricional.html')

@login_required  
def socioeconomico(request):
    return render(request, 'socioeconomico.html')

@login_required  
def tareas(request):
    tareas = Tareas.objects.filter(user=request.user, completado__isnull=True)
    return render(request, 'tareas.html', {
        'tareas': tareas
    })

@login_required  
def tarea_crear(request):
    if request.method == 'GET':
        return render(request, 'tarea_crear.html', {
            'form': TareaForm
        })
    else:
        try:
            form = TareaForm(request.POST)
            new_tarea = form.save(commit=False)
            new_tarea.user = request.user
            new_tarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea_crear.html', {
            'form': TareaForm,
            'error': 'Datos incorectos, Favor verificar la información'
            })

@login_required      
def tarea_detalle(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tareas, pk=tarea_id, user=request.user)
        form = TareaForm(instance=tarea)
        return render(request, 'tarea_detalle.html',{
            'tarea':tarea,
            'form': form
        })
    else:
        try:
            tarea = get_object_or_404(Tareas, pk=tarea_id, user=request.user)
            form = TareaForm(request.POST, instance=tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea_detalle.html',{
            'tarea':tarea,
            'form': form,
            'error': "Error al actualizar la Tarea"
        })

@login_required  
def tarea_completada(request):
    tareas = Tareas.objects.filter(user=request.user, completado__isnull=False).order_by('-completado')
    return render(request, 'tarea_completada.html', {
        'tareas': tareas
    })

@login_required  
def tarea_complatar(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.completado = timezone.now()
        tarea.save()
        return redirect('tareas')

@login_required  
def tarea_eliminar(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')


