from django.shortcuts import render, redirect, get_object_or_404
from beneficiario.forms import BeneficiarioForm, AntropBenefForm, AntropBenefRiesgoForm
from beneficiario.forms import MenorForm, FamiliarForm, MedicamentoForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from datetime import datetime

# Create your views here.
@login_required      
def beneficiario(request):
    beneficiarios = Beneficiario.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(beneficiarios, 2)
        beneficiarios = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'beneficiario.html',{
        'entity': beneficiarios,
        'paginator': paginator
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
        antropBefs = AntropBef.objects.filter(cedula_bef = pk)
        menores = Menor.objects.filter(cedula_bef=pk)
        familias = Familia.objects.filter(cedula_bef = pk)
        medicamentos = Medicamento.objects.filter(cedula_bef=pk)
        
        form = BeneficiarioForm(instance=beneficiarios)

        return render(request, 'beneficiario_detalle.html',{
            'beneficiarios':beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'form': form,
            'pk': pk

        })
  

@login_required      
def beneficiario_actualizar(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk, user=request.user)
        form = BeneficiarioForm(instance=beneficiarios)
        return render(request, 'beneficiario_actualizar.html',{
            'beneficiarios':beneficiarios,
            'form': form,
            'pk': pk
      })
    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk, user=request.user)
            form = BeneficiarioForm(request.POST, instance=beneficiarios)
            form.save()

            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            antropBefs = AntropBef.objects.filter(cedula_bef = pk)
            menores = Menor.objects.filter(cedula_bef=pk)
            familias = Familia.objects.filter(cedula_bef = pk)
            medicamentos = Medicamento.objects.filter(cedula_bef=pk)
   
            return render(request, 'beneficiario_detalle.html', {
            'beneficiarios': beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'pk': pk
                })
        except ValueError:
            return render(request, 'beneficiario_actualizar.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
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

            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            antropBefs = AntropBef.objects.filter(cedula_bef = pk)
            menores = Menor.objects.filter(cedula_bef=pk)
            familias = Familia.objects.filter(cedula_bef = pk)
            medicamentos = Medicamento.objects.filter(cedula_bef=pk)
   
            return render(request, 'beneficiario_detalle.html', {
            'beneficiarios': beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'pk': pk
                })
        except ValueError:
            return render(request, 'menor_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })


@login_required      
def menor_detalle(request, pk):
    if request.method == 'GET':
     
        menor_detalles = get_object_or_404(Menor, id=pk)
        print(pk)
        beneficiarios = Beneficiario.objects.filter(id=pk)
        antropBefs = AntropBef.objects.filter(cedula_bef = pk)
        menores = Menor.objects.filter(cedula_bef=pk)
        familias = Familia.objects.filter(cedula_bef = pk)
        medicamentos = Medicamento.objects.filter(cedula_bef=pk)
        
        form = MenorForm(instance=menor_detalles)
        page = request.GET.get('page',1)
        try:
            paginator1 = Paginator(antropBefs, 5)
            antropBefs = paginator1.page(page)
            paginator2 = Paginator(menores, 5)
            menores = paginator2.page(page)
            paginator3 = Paginator(familias, 5)
            familias = paginator3.page(page)
            paginator4 = Paginator(medicamentos, 5)
            medicamentos= paginator4.page(page)
        except:
            raise Http404
    
        return render(request, 'menor_detalle.html',{
            'menor_detalles': menor_detalles,
            'beneficiarios': beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'form': form,
            'pk': pk,
            'paginator1': paginator1,
            'paginator2': paginator2,
            'paginator3': paginator3,
            'paginator4': paginator4,
        })


# Sesion del Familiar

@login_required  
def familiar_crear(request,pk):
    if request.method == 'GET':
        return render(request, 'familiar_crear.html', {
            'form': FamiliarForm,
            'pk':pk
        })
    else:
        try:
            form = FamiliarForm(request.POST)
            new_familiar = form.save(commit=False)
            new_familiar.user = request.user
            new_familiar.save()

            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            antropBefs = AntropBef.objects.filter(cedula_bef = pk)
            menores = Menor.objects.filter(cedula_bef=pk)
            familias = Familia.objects.filter(cedula_bef = pk)
            medicamentos = Medicamento.objects.filter(cedula_bef=pk)

            return render(request, 'beneficiario_detalle.html', {
            'beneficiarios': beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'pk': pk
                })
        except ValueError:
            return render(request, 'familiar_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })


# Sesion Antropometrico del Beneficiario

@login_required  
def antrop_benef_crear(request,pk):
    context = {}
    if request.method=="POST":
        peso = float(request.POST.get("peso"))
        altura = float(request.POST.get("altura"))

    imc = (peso/(altura**2))
    save = request.POST.get("save")

    return


# Sesion de Medicamento 

@login_required  
def medicamento_crear(request,pk):
    if request.method == 'GET':
        return render(request, 'medicamento_crear.html', {
            'form': MedicamentoForm,
            'pk':pk
        })
    else:
        try:
            form = MedicamentoForm(request.POST)
            new_medicamento = form.save(commit=False)
            new_medicamento.save()

            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            antropBefs = AntropBef.objects.filter(cedula_bef = pk)
            menores = Menor.objects.filter(cedula_bef=pk)
            familias = Familia.objects.filter(cedula_bef = pk)
            medicamentos = Medicamento.objects.filter(cedula_bef=pk)
   
            return render(request, 'beneficiario_detalle.html', {
            'beneficiarios': beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'pk': pk
            })
        except ValueError:
            return render(request, 'menor_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })
