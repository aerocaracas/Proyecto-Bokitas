from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Nutricional, Jornada
from nutricional.forms import NutricionalForm
from django.core.paginator import Paginator
from nutricional.forms import NutricionalForm,NutricionalForm2
from django.contrib import messages


# Sesion Nutricional.
@login_required  
def nutricional(request):

    nutricionales = Nutricional.objects.all()
    query = ""
    page = request.GET.get('page',1)

    try:
        if "search" in request.POST:
            query = request.POST.get("searchquery")
            nutricionales = Nutricional.objects.filter(cedula_bef__cedula__contains=query)
        paginator = Paginator(nutricionales, 15)
        nutricionales = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'nutricional.html',{
        'entity': nutricionales,
        'query': query,
        'paginator': paginator
    })


@login_required  
def nutricional_crear(request):
    if request.method == 'GET':
        return render(request, 'nutricional_crear.html', {
            'form': NutricionalForm, 
        })
    else:
        try:
            form = NutricionalForm(request.POST)

            new_nutricional = form.save(commit=False)
            cedula = new_nutricional.cedula_bef_id
            beneficiario = get_object_or_404(Beneficiario, id=cedula)
            new_nutricional.proyecto_id = beneficiario.proyecto_id
            new_nutricional.save()
            messages.success(request, "Se guardo satisfactoriamente el Registro")
            return redirect('nutricional')
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'nutricional_crear.html', {
            'form': form,
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
    return render(request, "jornadas_options.html", {"jornadas": jornadas})
