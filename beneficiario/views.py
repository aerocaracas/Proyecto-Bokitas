from django.shortcuts import render, redirect, get_object_or_404
from beneficiario.forms import BeneficiarioForm, AntropBenefForm
from beneficiario.forms import MenorForm, FamiliarForm, MedicamentoForm, MedicaForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from datetime import datetime, date
from dateutil import relativedelta

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
def menor_crear(request, pk):
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
def menor_detalle(request, pk, id):

    print(pk)
    print(id)
    
    if request.method == 'GET':
     
        menor_detalles = get_object_or_404(Menor, id=pk)

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
def familiar_crear(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        fechaActual = datetime.now()
        context={}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios
        context["form"]=FamiliarForm
        context["fechaActual"]=fechaActual
        return render(request, 'familiar_crear.html', context)
    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            form = FamiliarForm(request.POST)
            new_familiar = form.save(commit=False)

            fecha_inicial = new_familiar.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)

            new_familiar.user = request.user 
            new_familiar.edad = tiempo_transc.years
            new_familiar.meses = tiempo_transc.months
            new_familiar.cedula_bef_id = pk
            new_familiar.save()

            print(tiempo_transc.years)
            print(tiempo_transc.months)

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

            return render(request, 'beneficiario_detalle.html', context)
        except ValueError:
            return render(request, 'familiar_crear.html', {
            'form': form,
            'beneficiarios':beneficiarios,
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })


# Sesion Antropometrico del Beneficiario

@login_required     
def imc_benef_riesgo(request, pk, idimc):
        
    if request.method == 'GET':

        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        imc_beneficiarios = get_object_or_404(AntropBef, id=idimc)
        context = {}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios
        context["idimc"]=idimc
        context["imc_beneficiarios"]=imc_beneficiarios

        return render(request, "imc_benef_riesgo.html", context)   

    if request.method=="POST":
        try:
            riesgo = request.POST.get("riesgo")
            servicio = request.POST.get("servicio")
            centro_hospital = request.POST.get("centro_hospital")
            observacion = request.POST.get("observacion")
        
            riesgos = get_object_or_404(AntropBef, id=idimc)
            riesgos.riesgo=riesgo
            riesgos.servicio=servicio
            riesgos.centro_hospital=centro_hospital
            riesgos.observacion=observacion          
            riesgos.save()

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
        
        except ValueError:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            imc_beneficiarios = get_object_or_404(AntropBef, id=idimc)
            context = {}
            context["pk"]=pk
            context["beneficiarios"]=beneficiarios
            context["idimc"]=idimc
            context["imc_beneficiarios"]=imc_beneficiarios
            context["error"]='Datos incorectos, Favor verificar la información'
            return render(request, 'imc_benef_riesgo.html', context)
    

@login_required 
def imc_benef(request, pk):
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

            imc = round(peso/(talla**2))

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

            antropometrico = AntropBef(cedula_bef_id=pk, fecha = fecha, embarazo_lactando=estado, tiempo_gestacion=tiempo, peso=peso, talla=talla, cbi=float(cbi), imc=imc, diagnostico=diagnostico)
            
            antropometrico.save()
            idimc=antropometrico.id

            return redirect("imc_benef_riesgo", pk, idimc)
        
        except ValueError:
            return render(request, 'imc_benef.html', {
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })


@login_required 
def imc_benef_detalle(request, pk, id):

    if request.method == 'GET':

        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        imc_beneficiarios = get_object_or_404(AntropBef, id=id)
        context = {}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios
        context["idimc"]=id
        context["imc_beneficiarios"]=imc_beneficiarios

        return render(request, "imc_benef_detalle.html", context)   


@login_required   
def imc_benef_eliminar(request, pk, id):
    imc_beneficiarios = get_object_or_404(AntropBef, id=id)
    imc_beneficiarios.delete()
    return redirect('beneficiario_detalle', pk)



# Sesion de Medicamento 

@login_required  
def medicamento_crear(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        context={}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios

        return render(request, 'medicamento_crear.html', context)
    else:
        try:
            medicamento = request.POST.get("medicamento")
            descripcion = request.POST.get("descripcion")
            cantidad = request.POST.get("cantidad")
            fecha = datetime.now()
            
            medicamentos = Medicamento(cedula_bef_id=pk, fecha = fecha, nombre=medicamento, descripcion=descripcion, cantidad=cantidad)
            medicamentos.save()

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
            
            return render(request, 'beneficiario_detalle.html', context)
        
        except ValueError:
            return render(request, 'menor_crear.html', {
            'beneficiarios': beneficiarios,
            'error': 'Datos incorectos, Favor verificar la información',
            'pk': pk
            })


@login_required 
def medicamento_eliminar(request, pk, id):

    medicamentos = get_object_or_404(Medicamento, id=id)
    medicamentos.delete()
    return redirect('beneficiario_detalle', pk)



# Sesion de Medica 

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

