from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Nutricional, Jornada
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from nutricional.forms import NutricionalForm, NutricionalForm2, ExpJornadaForm
from beneficiario.forms import ExpProyectoForm
from django.contrib import messages


# Sesion Nutricional.
@login_required  
def nutricional(request):

    if "search" in request.POST:
            query = request.POST.get("searchquery")
            nutricionales = Nutricional.objects.filter(Q(cedula_bef__cedula__icontains=query)).order_by('cedula_bef')
    else:
        query = ""
        nutricionales = Nutricional.objects.all().order_by('cedula_bef')

    expProyectoForm = ExpProyectoForm
    expJornadaForm = ExpJornadaForm
    paginator = Paginator(nutricionales, 10)
    page_number = request.GET.get('page')
    
    try:
        nutricionales = paginator.page(page_number)
    except PageNotAnInteger:
        nutricionales = paginator.page(1)
    except EmptyPage:
        nutricionales = paginator.page(paginator.num_pages)
    
    return render(request, 'nutricional.html',{
        'entity': nutricionales,
        'expProyectoForm':expProyectoForm,
        'expJornadaForm':expJornadaForm,
        'query':query,
        'paginator': paginator
    })


@login_required  
def nutricional_crear(request):
    if request.method == 'GET':
        return render(request, 'nutricional_crear.html', {
            'form': NutricionalForm 
        })
    else:
        try:
            form = NutricionalForm(request.POST)
            jornada_id = request.POST.get('jornada')
            form.fields['jornada'].choices = [(jornada_id, jornada_id)]
            
            if form.is_valid():
                
                new_nutricional = form.save(commit=False)
                cedula = new_nutricional.cedula_bef_id
                beneficiario = get_object_or_404(Beneficiario, id=cedula)
                new_nutricional.proyecto = beneficiario.proyecto
                new_nutricional.save()
                messages.success(request, "Se guardo satisfactoriamente el Registro")
                return redirect('nutricional')
            else:
                print("No es Valido!!!")
                print(form.errors)
                print(request.POST)
                messages.warning(request, "Datos incorectos, Favor verificar la información")
                return render(request, 'nutricional_crear.html', {
                'form': form
                })
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'nutricional_crear.html', {
            'form': form
            })


@login_required      
def nutricional_actualizar(request, pk):
    if request.method == 'GET':
        nutricionales = get_object_or_404(Nutricional, id=pk)
        form = NutricionalForm(instance=nutricionales)

        context={}
        context["pk"]=pk
        context["nutricionales"]=nutricionales
        context["form"]=form
        return render(request, 'nutricional_actualizar.html', context)
    else:
        try:
            nutricionales = get_object_or_404(Nutricional, id=pk)
            form = NutricionalForm2(request.POST, instance=nutricionales)

            new_nutricional = form.save(commit=False)

            new_nutricional.save()
            messages.success(request, "Se actualizo satisfactoriamente el Registro")
            return redirect('nutricional')
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'nutricional_actualizar.html', {
            'form': form,
            'pk': pk,
            })


@login_required   
def nutricional_eliminar(request, pk):
    nutricionales = get_object_or_404(Nutricional, id=pk)
    nutricionales.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")
    return redirect('nutricional')


def load_jornadas_nutri(request):
    beneficiario_id = request.GET.get("cedula_bef")
    proyecto_id = Beneficiario.objects.get(id=beneficiario_id).proyecto_id
    jornadas = Jornada.objects.filter(proyecto_id=proyecto_id)
    return render(request, "jornadas_nutricional.html", {"jornadas": jornadas})

def load_jornadas(request):
    proyecto_id = request.GET.get("proyecto")
    jornadas = Jornada.objects.filter(proyecto_id=proyecto_id)
    return render(request, "jornadas_options.html", {"jornadas": jornadas})

