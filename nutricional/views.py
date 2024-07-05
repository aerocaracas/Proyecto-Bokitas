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
        paginator = Paginator(nutricionales, 15)
        nutricionales = paginator.page(page)
    except:
        raise Http404

    return render(request, 'nutricional.html',{
        'entity': nutricionales,
        'paginator': paginator
    })


@login_required  
def nutricional_crear(request):
    if request.method == 'GET':
        return render(request, 'beneficiario_crear.html', {
            'form': NutricionalForm 
        })
    else:
        try:
            form = NutricionalForm(request.POST)
            new_beneficiario = form.save(commit=False)

            fecha_inicial = new_beneficiario.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)
            
            new_beneficiario.edad = tiempo_transc.years
            new_beneficiario.meses = tiempo_transc.months
            new_beneficiario.user = request.user
            new_beneficiario.save()

            return redirect('beneficiario')
        except ValueError:
            return render(request, 'beneficiario_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información'
            })
