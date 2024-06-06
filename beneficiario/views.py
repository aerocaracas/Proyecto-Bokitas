from django.shortcuts import render, redirect, get_object_or_404
from beneficiario.forms import BeneficiarioForm, AntropBenefForm, AntropBenefRiesgoForm
from beneficiario.forms import MenorForm, FamiliarForm, MedicamentoForm, MedicaForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from datetime import datetime

# Sesion del Beneficiario.
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
    
        return render(request, 'menor_detalle.html',{
            'menor_detalles': menor_detalles,
            'beneficiarios': beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'form': form,
            'pk': pk,
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


def imc(request):
    context = {}
    if request.method=="POST":
        peso_metric = request.POST.get("peso")
        if peso_metric:
            peso = float(request.POST.get("peso"))
            altura = float(request.POST.get("altura"))

        imc = (peso/(altura**2))

        if imc < 18.5:
            diagnostico = "PESO BAJO"
        elif imc >= 18.5 and imc < 25:
            diagnostico = "ADECUADO"
        elif imc >= 25 and imc < 30:
            diagnostico = "SOBREPESO"
        elif imc >= 30:
            diagnostico = "OBESIDAD"
        
        save = request.POST.get("save")
        if save=="on":
            AntropBef.objects.create(peso=peso, altura=altura, imc=round(imc), diagnostico=diagnostico)
        
        context["imc"] = round(imc)
        context["diagnostico"] = diagnostico
       

    return render(request, "imc.html", context)
 


@login_required  
def antrop_benef_crear(request,pk):
    if request.method == 'GET':
        return render(request, 'antrop_benef_crear.html', {
            'form': AntropBenefForm,
            'pk':pk
        })
    else:
        try:
            form = AntropBenefForm(request.POST)
            new_antropBenef = form.save(commit=False)
            new_antropBenef.save()
            return redirect('antrop_benef_calcular', {
                'pk': pk
            })
        except ValueError:
            return render(request, 'antrop_benef_crear.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información'
            })


@login_required  
def antrop_benef_calcular(request,pk):
    if request.method == 'GET':

        antropBenefs = get_object_or_404(AntropBef, id=pk)
        form = AntropBenefRiesgoForm
        
        return render(request, 'antrop_benef_calcular.html', {
            'antropBenefs':antropBenefs,
            'form': form,
            'pk': pk
      })
    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            form = AntropBenefRiesgoForm(request.POST) 
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
            return render(request, 'antrop_benef_actualizar.html', {
            'form': form,
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })

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

