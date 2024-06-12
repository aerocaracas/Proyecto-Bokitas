from django.shortcuts import render, redirect, get_object_or_404
from beneficiario.forms import BeneficiarioForm, AntropBenefForm
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

@login_required 
def imc_benef(request,pk):
    if request.method == 'GET':

        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        context = {}
        context["pk"] = pk
        context["beneficiarios"] = beneficiarios
    
        return render(request, "imc_benef.html", context)

    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)

            peso = float(request.POST.get("peso"))
            talla = float(request.POST.get("talla"))
            cbi = request.POST.get("cbi")
            tiempo = request.POST.get("tiempo")

            talla = talla/100

            imc = (peso/(talla**2))

            if imc < 18.5:
                diagnostico = "PESO BAJO"
            elif imc >= 18.5 and imc < 23:
                diagnostico = "ADECUADO"
            elif imc >= 23 and imc < 25:
                diagnostico = "RIESGO DE SOBREPESO"
            elif imc >= 25 and imc < 30:
                diagnostico = "SOBREPESO"
            elif imc >= 30:
                diagnostico = "OBESIDAD"

            fecha = datetime.now()
            if beneficiarios.embarazada == "SI":
                estado = "EMBARAZADA"
            elif beneficiarios.lactando == "SI":
                estado = "LACTANDO"
            else:
                estado = "ESTUDIO"

            antropometrico = AntropBef(cedula_bef_id=pk, fecha = fecha, embarazo_lactando=estado, tiempo_gestacion=tiempo, peso=peso, talla=talla, cbi=cbi, imc=round(imc), diagnostico=diagnostico)
            
            antropometrico.save()
            idimc=antropometrico.id

            context={}
            context["pk"]= pk
            context["idimc"]=idimc
            context["beneficiarios"] = beneficiarios
            context["peso"]=peso
            context["talla"]=talla
            context["cbi"]=cbi
            context["imc"]=imc
            context["diagnostico"]=diagnostico

            return render(request, "imc_benef_resul.html", context)
        
        except ValueError:
            return render(request, 'imc_benef.html', {
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })
    

@login_required     
def imc_benef_resul(request,pk):   

    if request.method=="POST":

        riesgo = request.POST.get("riesgo")
        servicio = request.POST.get("servicio")
        centro_hospital = request.POST.get("centro_hospital")
        observacion = request.POST.get("observacion")
        

        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        antropBefs = AntropBef.objects.filter(cedula_bef = pk)
        menores = Menor.objects.filter(cedula_bef=pk)
        familias = Familia.objects.filter(cedula_bef = pk)
        medicamentos = Medicamento.objects.filter(cedula_bef=pk)
        context={}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios
        context["antropBefs"]=antropBefs
        context["menores"]=menores
        context["familias"]=familias
        context["medicamentos"]=medicamentos

    return render(request, "beneficiario_detalle.html", context)
 

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

