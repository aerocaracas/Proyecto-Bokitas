from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from tareas.forms import TareaForm
from bokitas.models import Tarea
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required  
def tareas(request):
    tareas = Tarea.objects.filter(user=request.user, completado__isnull=True)
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
        tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
        form = TareaForm(instance=tareas)
        return render(request, 'tarea_detalle.html',{
            'tareas':tareas,
            'form': form
        })
    else:
        try:
            tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
            form = TareaForm(request.POST, instance=tareas)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea_detalle.html',{
            'tareas':tareas,
            'form': form,
            'error': "Error al actualizar la Tarea"
        })

@login_required  
def tarea_completada(request):
    tareas = Tarea.objects.filter(user=request.user, completado__isnull=False).order_by('-completado')
    return render(request, 'tarea_completada.html', {
        'tareas': tareas
    })

@login_required  
def tarea_complatar(request, tarea_id):
    tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tareas.completado = timezone.now()
        tareas.save()
        return redirect('tareas')

@login_required  
def tarea_eliminar(request, tarea_id):
    tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tareas.delete()
        return redirect('tareas')

