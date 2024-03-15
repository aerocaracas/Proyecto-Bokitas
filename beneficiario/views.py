from django.shortcuts import render, redirect, get_object_or_404
from beneficiario.forms import BeneficiarioForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario
from django.contrib.auth.models import User

# Create your views here.
@login_required      
def beneficiario(request):
    beneficiarios = Beneficiario.objects.all()
    return render(request, 'beneficiario.html',{
        'beneficiarios': beneficiarios
    })


@login_required  
def beneficiario_crear(request):
    if request.method == 'GET':
        return render(request, 'beneficiario_crear.html', {
            'form': BeneficiarioForm
        })
    else:
        try:
            form = BeneficiarioForm(request.POST)
            new_beneficiario = form.save(commit=False)
            new_beneficiario.user = request.user
            new_beneficiario.save()
            return redirect('beneficiario')
        except ValueError:
            return render(request, 'beneficiario_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información'
            })

@login_required      
def beneficiario_detalle(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        form = BeneficiarioForm(instance=beneficiarios)
        return render(request, 'beneficiario_detalle.html',{
            'beneficiarios':beneficiarios,
            'form': form
        })

@login_required      
def beneficiario_actualizar(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk, user=request.user)
        form = BeneficiarioForm(instance=beneficiarios)
        return render(request, 'beneficiario_actualizar.html',{
            'beneficiarios':beneficiarios,
            'form': form
      })
    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk, user=request.user)
            form = BeneficiarioForm(request.POST, instance=beneficiarios)
            form.save()
            return redirect('beneficiario')
        except ValueError:
            return render(request, 'beneficiario_actualizar.html',{
            'beneficiarios':beneficiarios,
            'form': form,
            'error': "Error al actualizar al Beneficiario"
        })

@login_required   
def beneficiario_eliminar(request, pk):
    beneficiarios = get_object_or_404(Beneficiario, id=pk)
    beneficiarios.delete()
    return redirect('beneficiario')

