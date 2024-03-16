from django.shortcuts import render, redirect, get_object_or_404
from beneficiario.forms import BeneficiarioForm, MenorForm, FamiliarForm, AntropBenefForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, Antropometrico
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

        antropometricos = Antropometrico.objects.filter(cedula_bef = pk)

        menores = Menor.objects.filter(cedula_bef=pk)

        familias = Familia.objects.filter(cedula_bef = pk)
        
        form = BeneficiarioForm(instance=beneficiarios)
        return render(request, 'beneficiario_detalle.html',{
            'beneficiarios':beneficiarios,
            'antropometricos': antropometricos,
            'menores': menores,
            'familias': familias,
            'form': form,
            'pk': pk,
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



# Sesion de Menores 

@login_required  
def menor_crear(request,pk):
    if request.method == 'GET':
        return render(request, 'menor_crear.html', {
            'form': MenorForm,
            'pk':pk
        })
    else:
        try:
            form = MenorForm(request.POST)
            new_menor = form.save(commit=False)
            new_menor.user = request.user
            new_menor.save()
            
                
            return render(request, 'beneficiario_detalle.html', {
                'pk': pk
                })
        except ValueError:
            return render(request, 'menor_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información'
            })




# Sesion del Familiar

@login_required  
def familiar_crear(request):
    if request.method == 'GET':
        return render(request, 'familiar_crear.html', {
            'form': FamiliarForm
        })
    else:
        try:
            form = FamiliarForm(request.POST)
            new_familiar = form.save(commit=False)
            new_familiar.user = request.user
            new_familiar.save()
            return redirect('beneficiario_detalle')
        except ValueError:
            return render(request, 'familiar_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información'
            })


# Sesion Antropometrico de Beneficiario

@login_required  
def antrop_benef_crear(request):
    if request.method == 'GET':
        return render(request, 'antrop_bene_crear.html', {
            'form': AntropBenefForm
        })
    else:
        try:
            form = AntropBenefForm(request.POST)
            new_antrop = form.save(commit=False)
            new_antrop.user = request.user
            new_antrop.save()
            return redirect('beneficiario_detalle')
        except ValueError:
            return render(request, 'antrop_bene_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información'
            })

