from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from bokitas.models import Nutricional,Beneficiario
from nutricional.forms import NutricionalForm
from django.core.paginator import Paginator
from datetime import datetime, date
from dateutil import relativedelta

# Sesion Nutricional.
@login_required  
def nutricional(request):
    nutricionales = Nutricional.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(nutricionales, 3)
        nutricionales = paginator.page(page)
    except:
        raise Http404

    return render(request, 'nutricional.html',{
        'entity': nutricionales,
        'paginator': paginator,

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
            print(cedula)
            beneficiario = get_object_or_404(Beneficiario, id=cedula)
            new_nutricional.proyecto_id = beneficiario.proyecto_id
            new_nutricional.save()

            return redirect('nutricional')
        except ValueError:
            return render(request, 'nutricional_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información'
            })
