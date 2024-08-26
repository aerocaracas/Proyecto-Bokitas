from django.shortcuts import render, redirect, get_object_or_404
from proyecto.forms import ProyectoForm, JornadaForm, ExpJornadaForm
from beneficiario.forms import ExpProyectoForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Proyecto, Jornada
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages

# Create your views here.
@login_required      
def proyecto(request):
    proyectos = Proyecto.objects.all()
    proyect = ExpProyectoForm
    expJornadaForm = ExpJornadaForm()
    query = ""
    page = request.GET.get('page',1)

    try:
        if "search" in request.POST:
            query = request.POST.get("searchquery")
            proyectos = Proyecto.objects.filter(Q(proyecto__icontains=query))
            paginator = Paginator(proyectos, 10)
            proyectos = paginator.page(page)
            return render(request, 'proyecto.html',{
                'entity': proyectos,
                'proyect':proyect,
                'expJornadaForm':expJornadaForm,
                'query':query,
                'paginator': paginator
                })
        paginator = Paginator(proyectos, 10)
        proyectos = paginator.page(page)
        if request.method == 'POST':
            expJornadaForm = ExpJornadaForm(request.POST)
            if expJornadaForm.is_valid():
                print('test test')
                expJornadaForm.save()
                return redirect('pryectos')

        
    except:
        raise Http404

    return render(request, 'proyecto.html',{
        'entity': proyectos,
        'proyect':proyect,
        'expJornadaForm':expJornadaForm,
        'query':query,
        'paginator': paginator
    })


# AJAX
def load_jornadas(request):
    country_id = request.GET.get('proyecto_id')
    cities = Jornada.objects.filter(proyecto_id=country_id).all()
    return render(request, 'load_jornadas.html', {'jornadas': cities})



@login_required      
def proyecto_detalle(request, pk):
    if request.method == 'GET':
     
        proyectos = get_object_or_404(Proyecto, id=pk)
        jornadas = Jornada.objects.filter(proyecto = pk).order_by('jornada')
        
        form = ProyectoForm(instance=proyectos)
        formJornada = JornadaForm

       
        return render(request, 'proyecto_detalle.html',{
            'proyectos':proyectos,
            'jornadas':jornadas,
            'form': form,
            'formJornada': formJornada,
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
            'form': form,
            'pk': pk
        })
    else:
        try:
            proyectos = get_object_or_404(Proyecto, id=pk, user=request.user)
            form = ProyectoForm(request.POST, instance=proyectos)
            form.save()
            messages.success(request, "Se actualizo satisfactoriamente el Proyecto")
            return redirect('proyecto_detalle', pk)
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


@login_required  
def proyecto_jornada(request, pk):
        try:
            formulario = JornadaForm(request.POST)
            new_jornada = formulario.save(commit=False)
            new_jornada.proyecto_id = pk
            new_jornada.save()
            messages.success(request, "Se creo agrego nueva fecha al Proyecto")
            return redirect('proyecto_detalle',pk)
        except ValueError:
            proyectos = get_object_or_404(Proyecto, id=pk)
            formJornada = JornadaForm
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'proyecto_detalle.html', {
            'formJornada': formJornada,
            'proyectos':proyectos,
            'pk': pk
            })


@login_required   
def jornada_eliminar(request, pk, id):
    jornadas = get_object_or_404(Jornada, id=id)
    jornadas.delete()
    messages.error(request, "Se Elimino satisfactoriamente la Jornada")
    return redirect('proyecto_detalle',pk)


