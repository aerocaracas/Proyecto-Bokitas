from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from tareas.forms import TareaForm
from bokitas.models import Tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

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

