from django.shortcuts import render, redirect, get_object_or_404
from medica.forms import MedicaForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Medica
from django.contrib.auth.models import User

# Create your views here.
@login_required      
def medica(request):
    medicas = Medica.objects.all()
    return render(request, 'medica.html',{
        'medicas': medicas
    })

@login_required  
def medica_crear(request):
    if request.method == 'GET':
        return render(request, 'medica_crear.html', {
            'form': MedicaForm
        })
    else:
        try:
            form = MedicaForm(request.POST)
            new_medica = form.save(commit=False)
            new_medica.user = request.user
            new_medica.save()
            return redirect('medica')
        except ValueError:
            return render(request, 'medica_crear.html', {
            'form': MedicaForm,
            'error': 'Datos incorectos, Favor verificar la información'
            })

@login_required      
def medica_detalle(request, pk):
    if request.method == 'GET':
        medicas = get_object_or_404(Medica, id=pk, user=request.user)
        form = MedicaForm(instance=medicas)
        return render(request, 'medica_detalle.html',{
            'medicas':medicas,
            'form': form
        })
    else:
        try:
            medicas = get_object_or_404(Medica, id=pk, user=request.user)
            form = MedicaForm(request.POST, instance=medicas)
            form.save()
            return redirect('medica')
        except ValueError:
            return render(request, 'medica_detalle.html',{
            'medicas':medicas,
            'form': form,
            'error': "Error al actualizar el formulario"
        })

@login_required   
def medica_eliminar(request, pk):
    medicas = get_object_or_404(Medica, id=pk, user=request.user)
    if request.method == 'POST':
        medicas.delete()
        return redirect('medica')

