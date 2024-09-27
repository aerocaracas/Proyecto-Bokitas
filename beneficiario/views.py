from django.shortcuts import render, redirect, get_object_or_404
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, Medicamento, Nutricional, Proyecto, Jornada
from beneficiario.forms import BeneficiarioForm, ExpProyectoForm, ImcBenefForm, FamiliarForm, MedicamentosForm
from nutricional.forms import NutricionalForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from bokitas.models import ImcEmbarazada, Diagnostico
from django.contrib.auth.models import User
from django.http import Http404
from datetime import datetime, date
from dateutil import relativedelta
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Sesion del Beneficiario.
@login_required      
def beneficiario(request):

    if "search" in request.POST:
            query = request.POST.get("searchquery")
            beneficiarios = Beneficiario.objects.filter(Q(cedula__icontains=query) | Q(proyecto__proyecto__icontains=query) | Q(nombre__icontains=query) | Q(apellido__icontains=query)).order_by('cedula')
    else:
        query = ""
        beneficiarios = Beneficiario.objects.all().order_by('cedula')

    proyect = ExpProyectoForm
    paginator = Paginator(beneficiarios, 10)
    page_number = request.GET.get('page')
    

    try:
        beneficiarios = paginator.page(page_number)
    except PageNotAnInteger:
        beneficiarios = paginator.page(1)
    except EmptyPage:
        beneficiarios = paginator.page(paginator.num_pages)
    
    return render(request, 'beneficiario.html',{
        'beneficiarios': beneficiarios,
        'proyect':proyect,
        'query':query,
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

            fecha_inicial = new_beneficiario.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)
                
            new_beneficiario.edad = tiempo_transc.years
            new_beneficiario.meses = tiempo_transc.months
            new_beneficiario.user = request.user
            new_beneficiario.save()
            messages.success(request, "Se creo satisfactoriamente el Beneficiario")
            return redirect('beneficiario')
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'beneficiario_crear.html', {
            'form': form,
            })


def load_jornadas_benef(request):
    proyecto_id = request.GET.get("proyecto")
    jornadas = Jornada.objects.filter(proyecto_id=proyecto_id)
    return render(request, "jornadas_options.html", {"jornadas": jornadas})


def load_jornadas_benef_act(request, pk):
    proyecto_id = request.GET.get("proyecto")
    jornadas = Jornada.objects.filter(proyecto_id=proyecto_id)
    return render(request, "jornadas_options.html", {"jornadas": jornadas})



@login_required     
def beneficiario_detalle(request, pk):
    if request.method == 'GET':
     
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        antropBefs = AntropBef.objects.filter(cedula_bef = pk)
        menores = Menor.objects.filter(cedula_bef=pk)
        familias = Familia.objects.filter(cedula_bef = pk)
        medicamentos = Medicamento.objects.filter(cedula_bef=pk)
        nutricionales = Nutricional.objects.filter(cedula_bef=pk)
        proyectos = get_object_or_404(Proyecto, id=beneficiarios.proyecto_id)
        
        form = BeneficiarioForm(instance=beneficiarios)

        return render(request, 'beneficiario_detalle.html',{
            'beneficiarios':beneficiarios,
            'antropBefs': antropBefs,
            'menores': menores,
            'familias': familias,
            'medicamentos': medicamentos,
            'nutricionales':nutricionales,
            'proyectos':proyectos,
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
            act_beneficiario = form.save(commit=False)

            fecha_inicial = act_beneficiario.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)
            
            act_beneficiario.edad = tiempo_transc.years
            act_beneficiario.meses = tiempo_transc.months
            act_beneficiario.user = request.user
            act_beneficiario.save()

            messages.success(request, "Se actualizo satisfactoriamente el Registro")
            return redirect("beneficiario_detalle", pk)
        
        
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'beneficiario_actualizar.html', {
            'form': form,
            'pk': pk
            })


@login_required   
def beneficiario_eliminar(request, pk):
    beneficiarios = get_object_or_404(Beneficiario, id=pk)
    beneficiarios.delete()
    messages.error(request, "Se Elimino satisfactoriamente al Beneficiario")
    return redirect('beneficiario')


# Sesion del Familiar

@login_required  
def familiar_crear(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        context={}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios
        context["form"]=FamiliarForm
        
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

            messages.success(request, "Se guardo satisfactoriamente el Registro")
            return redirect("beneficiario_detalle", pk)
            
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'familiar_crear.html', {
            'form': form,
            'beneficiarios':beneficiarios,
            'pk': pk
            })


@login_required      
def familiar_actualizar(request, pk, id):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        familias = get_object_or_404(Familia, id=id)
        form = FamiliarForm(instance=familias)
        context={}
        context["pk"]=pk
        context["idfam"]=id
        context["beneficiarios"]=beneficiarios
        context["familias"]=familias
        context["form"]=form
        return render(request, 'familiar_actualizar.html', context)
    else:
        try:
            familias = get_object_or_404(Familia, id=id, user=request.user)
            form = FamiliarForm(request.POST, instance=familias)
            new_familiar = form.save(commit=False)

            fecha_inicial = familias.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)

            new_familiar.edad = tiempo_transc.years
            new_familiar.meses = tiempo_transc.months

            new_familiar.save()

            messages.success(request, "Se actualizo satisfactoriamente el Registro")
            return redirect("beneficiario_detalle", pk)

        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'familia_actualizar.html', {
            'form': form,
            'pk': pk,
            'id': id
            })


@login_required   
def familiar_eliminar(request, pk, id):
    familias = get_object_or_404(Familia, id=id)
    familias.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")
    return redirect('beneficiario_detalle', pk)


# Sesion IMC del Beneficiario

@login_required     
def imc_benef_riesgo(request, pk, idimc):
        
    if request.method == 'GET':

        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        imc_beneficiarios = get_object_or_404(AntropBef, id=idimc)
        diag_imc = get_object_or_404(Diagnostico, diagnostico = imc_beneficiarios.diagnostico)
        imc = str(imc_beneficiarios.imc).replace(',','.')
        min_imc = str(imc_beneficiarios.min_imc).replace(',','.')
        max_imc = str(imc_beneficiarios.max_imc).replace(',','.')
        context = {}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios
        context["idimc"]=idimc
        context["imc"]=imc
        context["min_imc"]=min_imc
        context["max_imc"]=max_imc
        context["diag_imc"]=diag_imc
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

            messages.success(request, "Se guardo satisfactoriamente el Registro")
            return redirect('beneficiario_detalle', pk)
        
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            imc_beneficiarios = get_object_or_404(AntropBef, id=idimc)
            context = {}
            context["pk"]=pk
            context["beneficiarios"]=beneficiarios
            context["idimc"]=idimc
            context["imc_beneficiarios"]=imc_beneficiarios

            return render(request, 'imc_benef_riesgo.html', context)
    

@login_required 
def imc_benef(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        proyecto_id = beneficiarios.proyecto_id

        form = ImcBenefForm()
        form.fields['jornada'].queryset = Jornada.objects.filter(proyecto=proyecto_id)

        context={}
        context["pk"]=pk
        context["form"]=form
        context["beneficiarios"]=beneficiarios
    
        return render(request, "imc_benef.html", context)

    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            form = ImcBenefForm(request.POST)
            new_imc_benef = form.save(commit=False)

            talla = float(new_imc_benef.talla)
            peso = float(new_imc_benef.peso)
            cbi = new_imc_benef.cbi
            tiempo = new_imc_benef.tiempo_gestacion

            min_imc = 0
            max_imc = 0
            talla = talla/100

            imc = round(peso/(talla**2),2)

            if beneficiarios.embarazada == "SI":

                if tiempo >= 6 and tiempo <= 42:
                    xImc = ImcEmbarazada.objects.get(semana = tiempo)
                else:
                    messages.warning(request, "Datos incorectos, Favor verificar la información")
                    return render(request, 'imc_benef.html', {
                    'pk': pk,
                    'form': form,
                    'beneficiarios': beneficiarios
            })

                if xImc:                  
                    if imc <= xImc.p2:
                        xDiagnostico = 10
                        min_imc = float(xImc.p2) - 2
                        max_imc = xImc.p2
                    elif imc > xImc.p2 and imc <= xImc.p3:
                        xDiagnostico = 4
                        min_imc = xImc.p2
                        max_imc = xImc.p3
                    elif imc > xImc.p3 and imc <= xImc.p4:
                        xDiagnostico = 5
                        min_imc = xImc.p3
                        max_imc = xImc.p4
                    elif imc > xImc.p4 and imc <= xImc.p5:
                        xDiagnostico = 6
                        min_imc = xImc.p4
                        max_imc = xImc.p5
                    elif imc >= xImc.p5:
                        xDiagnostico = 7
                        min_imc = xImc.p5
                        max_imc = float(xImc.p5) + 2

            else:

                if imc < 18.5:
                    xDiagnostico = 10
                elif imc >= 18.5 and imc < 23:
                    xDiagnostico = 4
                elif imc >= 23 and imc < 25:
                    xDiagnostico = 5
                elif imc >= 25 and imc < 30:
                    xDiagnostico = 6
                elif imc >= 30:
                    xDiagnostico = 7

            if beneficiarios.embarazada == "SI":
                estado = "EMBARAZADA"
            elif beneficiarios.lactante == "SI":
                estado = "LACTANDO"
            else:
                estado = "ESTUDIO"

        #********   DIAGNOSTICO   **********

            xDiag = Diagnostico.objects.get(codigo_diag = xDiagnostico)
            diagnostico = xDiag.diagnostico


            fecha_inicial = beneficiarios.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)

            xEdad = tiempo_transc.years
            xMeses = tiempo_transc.months
            proyecto = beneficiarios.proyecto

            antropometrico = AntropBef(cedula_bef_id=pk, proyecto = proyecto, jornada = new_imc_benef.jornada, embarazo_lactando=estado, tiempo_gestacion=tiempo, edad=xEdad, meses=xMeses, peso=peso, talla=talla, cbi=float(cbi), imc=imc, diagnostico=diagnostico, min_imc = min_imc, max_imc = max_imc)
            
            antropometrico.save()
            idimc=antropometrico.id

            beneficiarios.edad = xEdad
            beneficiarios.meses = xMeses
            beneficiarios.save()

            return redirect("imc_benef_riesgo", pk, idimc)
        
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'imc_benef.html', {
            'pk': pk,
            'form': form,
            'beneficiarios': beneficiarios
            })


@login_required 
def imc_benef_detalle(request, pk, id):

    if request.method == 'GET':

        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        imc_beneficiarios = get_object_or_404(AntropBef, id=id)
        diag_imc = get_object_or_404(Diagnostico, diagnostico = imc_beneficiarios.diagnostico)
        imc = str(imc_beneficiarios.imc).replace(',','.')
        min_imc = str(imc_beneficiarios.min_imc).replace(',','.')
        max_imc = str(imc_beneficiarios.max_imc).replace(',','.')
        context = {}
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios
        context["idimc"]=id
        context["imc"]=imc
        context["min_imc"]=min_imc
        context["max_imc"]=max_imc
        context["diag_imc"]=diag_imc
        context["imc_beneficiarios"]=imc_beneficiarios

        return render(request, "imc_benef_detalle.html", context)   


@login_required   
def imc_benef_eliminar(request, pk, id):
    imc_beneficiarios = get_object_or_404(AntropBef, id=id)
    imc_beneficiarios.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")
    return redirect('beneficiario_detalle', pk)


# Sesion de Medicamento 

@login_required  
def medicamento_crear(request, pk):

    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        proyecto_id = beneficiarios.proyecto_id

        form = MedicamentosForm()
        form.fields['jornada'].queryset = Jornada.objects.filter(proyecto=proyecto_id)
        
        context={}
        context["form"]=form
        context["pk"]=pk
        context["beneficiarios"]=beneficiarios

        return render(request, 'medicamento_crear.html', context)
    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            form = MedicamentosForm(request.POST)
            new_dedicamento = form.save(commit=False) 
            new_dedicamento.cedula_bef_id = pk
            new_dedicamento.proyecto = beneficiarios.proyecto
            new_dedicamento.save()

            messages.success(request, "Se guardo satisfactoriamente el Registro")

            return redirect("beneficiario_detalle", pk)
        
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'menor_crear.html', {
            'beneficiarios': beneficiarios,
            'pk': pk,
            'form': form
            })


@login_required 
def medicamento_eliminar(request, pk, id):

    medicamentos = get_object_or_404(Medicamento, id=id)
    medicamentos.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")
    return redirect('beneficiario_detalle', pk)


# Sesion de Nutricional

@login_required      
def nutricional_beneficiario(request, pk, id):
    if request.method == 'GET':
        nutricionales = get_object_or_404(Nutricional, id=id)
        form = NutricionalForm(instance=nutricionales)

        context={}
        context["pk"]=pk
        context["id"]=id
        context["nutricionales"]=nutricionales
        context["form"]=form
        return render(request, 'nutricional_beneficiario.html', context)


