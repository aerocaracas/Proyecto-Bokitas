from django.shortcuts import render, redirect, get_object_or_404
from proyecto.forms import ProyectoForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Proyecto

# Create your views here.
@login_required      
def proyecto(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto.html',{
        'proyectos': proyectos
    })

@login_required      
def proyecto_detalle(request, proyectos_id):
    if request.method == 'GET':
        proyectos = get_object_or_404(Proyecto, pk=proyectos_id)
        form = ProyectoForm(instance=proyectos)
        return render(request, 'proyecto_detalle.html',{
            'proyectos':proyectos,
            'form': form
        })
    else:
        try:
            proyectos = get_object_or_404(Proyecto, pk=proyectos_id)
            form = ProyectoForm(request.POST, instance=proyectos)
            form.save()
            return redirect('proyecto')
        except ValueError:
            return render(request, 'proyecto_detalle.html',{
            'proyectos':proyectos,
            'form': form,
            'error': "Error al actualizar Proyecto"
        })
