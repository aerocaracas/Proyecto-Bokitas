from django.shortcuts import render, redirect, get_object_or_404
from proyecto.forms import ProyectoForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Proyecto
from django.contrib.auth.models import User

# Create your views here.
@login_required      
def proyecto(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto.html',{
        'proyectos': proyectos
    })


@login_required  
def proyecto_crear(request):
    if request.method == 'GET':
        return render(request, 'proyecto_crear.html', {
            'form': ProyectoForm
        })
    else:
        try:
            form = ProyectoForm(request.POST)
            new_proyecto = form.save(commit=False)
            new_proyecto.user = request.user
            new_proyecto.save()
            return redirect('proyecto')
        except ValueError:
            return render(request, 'proyecto_crear.html', {
            'form': ProyectoForm,
            'error': 'Datos incorectos, Favor verificar la información'
            })

@login_required      
def proyecto_detalle(request, pk):
    if request.method == 'GET':
        proyectos = get_object_or_404(Proyecto, id=pk, user=request.user)
        form = ProyectoForm(instance=proyectos)
        return render(request, 'proyecto_detalle.html',{
            'proyectos':proyectos,
            'form': form
        })
    else:
        try:
            proyectos = get_object_or_404(Proyecto, id=pk, user=request.user)
            form = ProyectoForm(request.POST, instance=proyectos)
            form.save()
            return redirect('proyecto')
        except ValueError:
            return render(request, 'proyecto_detalle.html',{
            'proyectos':proyectos,
            'form': form,
            'error': "Error al actualizar Proyecto"
        })

@login_required   
def proyecto_eliminar(request, pk):
    proyectos = get_object_or_404(Proyecto, id=pk, user=request.user)
    if request.method == 'POST':
        proyectos.delete()
        return redirect('proyecto')

