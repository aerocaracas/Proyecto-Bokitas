from django.shortcuts import render, redirect, get_object_or_404
from proyecto.forms import ProyectoForm
from beneficiario.forms import ExpProyectoForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Proyecto, Jornada
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages

# Create your views here.
@login_required      
def proyecto(request):
    proyectos = Proyecto.objects.all()
    proyect = ExpProyectoForm
    query = ""
    page = request.GET.get('page',1)

    try:
        if "search" in request.POST:
            query = request.POST.get("searchquery")
            proyectos = Proyecto.objects.filter(Q(proyecto__icontains=query))
        
        paginator = Paginator(proyectos, 2)
        proyectos = paginator.page(page)
    except:
        raise Http404

    return render(request, 'proyecto.html',{
        'entity': proyectos,
        'proyect':proyect,
        'query':query,
        'paginator': paginator
    })


@login_required      
def proyecto_detalle(request, pk):
    if request.method == 'GET':
     
        proyectos = get_object_or_404(Proyecto, id=pk)
        jornadas = Jornada.objects.filter(proyecto = pk)
        
        form = ProyectoForm(instance=proyectos)

        return render(request, 'proyecto_detalle.html',{
            'proyectos':proyectos,
            'jornadas':jornadas,
            'form': form,
            'pk': pk

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
            messages.success(request, "Se creo satisfactoriamente el Nuevo Proyecto")
            return redirect('proyecto')
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'proyecto_crear.html', {
            'form': form,
            })


@login_required      
def proyecto_actualizar(request, pk):
    if request.method == 'GET':
        proyectos = get_object_or_404(Proyecto, id=pk, user=request.user)
        form = ProyectoForm(instance=proyectos)
        return render(request, 'proyecto_actualizar.html',{
            'proyectos':proyectos,
            'form': form
        })
    else:
        try:
            proyectos = get_object_or_404(Proyecto, id=pk, user=request.user)
            form = ProyectoForm(request.POST, instance=proyectos)
            form.save()
            messages.success(request, "Se actualizo satisfactoriamente el Proyecto")
            return redirect('proyecto')
        except ValueError:
            messages.warning(request, "Error al actualizar Proyecto")
            return render(request, 'proyecto_actualizar.html',{
            'proyectos':proyectos,
            'form': form,
        })


@login_required   
def proyecto_eliminar(request, pk):
    proyectos = get_object_or_404(Proyecto, id=pk, user=request.user)
    proyectos.delete()
    messages.error(request, "Se Elimino satisfactoriamente el Proyecto")
    return redirect('proyecto')

