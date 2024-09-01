from django.shortcuts import render, redirect, get_object_or_404
from beneficiario.forms import BeneficiarioForm, ExpProyectoForm, ImcMenorForm, ImcBenefForm
from beneficiario.forms import MenorForm, FamiliarForm, MedicaForm, MedicamentosForm
from nutricional.forms import NutricionalForm
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica, Nutricional, Proyecto, Jornada
from django.db.models import Q
from bokitas.models import ImcCla, ImcEmbarazada, ImcPesoTalla_5x, ImcTalla, ImcCla_5x, Diagnostico
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from datetime import datetime, date
from dateutil import relativedelta
from django.contrib import messages

# Sesion del Beneficiario.
@login_required      
def beneficiario(request):
    beneficiarios = Beneficiario.objects.all().order_by('cedula')
    proyect = ExpProyectoForm
    query = ''

    page = request.GET.get('page',1)

    try:
        if "search" in request.POST:
            query = request.POST.get("searchquery")
            beneficiarios = Beneficiario.objects.filter(Q(cedula__icontains=query) | Q(nombre__icontains=query) | Q(apellido__icontains=query)).order_by('cedula')

        paginator = Paginator(beneficiarios, 10)
        beneficiarios = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'beneficiario.html',{
        'entity': beneficiarios,
        'proyect':proyect,
        'query':query,
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


# Sesion de Menores 

@login_required  
def menor_crear(request, pk):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        return render(request, 'menor_crear.html', {
            'form': MenorForm,
            'beneficiarios': beneficiarios,
            'pk':pk
        })
    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            form = MenorForm(request.POST)
            new_menor = form.save(commit=False)

            fecha_inicial = new_menor.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)

            new_menor.edad = tiempo_transc.years
            new_menor.meses = tiempo_transc.months
            new_menor.cedula_bef_id = pk
            new_menor.user = request.user
            new_menor.save()

            messages.success(request, "Se creo satisfactoriamente el Menor")
            return redirect("beneficiario_detalle", pk)
           
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'menor_crear.html', {
            'form': form,
            'pk': pk
            })


def load_jornadas_menor(request, pk):
    print('test')
    proyecto_id = request.GET.get("proyecto")
    jornadas = Jornada.objects.filter(proyecto_id=proyecto_id)
    return render(request, "jornadas_options.html", {"jornadas": jornadas})


@login_required      
def menor_detalle(request, pk, id):
    
    if request.method == 'GET':
     
        menor_detalles = get_object_or_404(Menor, id=id)
        beneficiarios = Beneficiario.objects.filter(id=pk)
        antropMenores = AntropMenor.objects.filter(cedula = id)
        medicas = Medica.objects.filter(cedula = id)
        proyectos = get_object_or_404(Proyecto, id=menor_detalles.proyecto_id)

        form = MenorForm(instance=menor_detalles)

        context={}
        context["pk"]=pk
        context["id"]=id
        context["form"]=form
        context["menor_detalles"]=menor_detalles
        context["beneficiarios"]=beneficiarios
        context["antropMenores"]=antropMenores
        context["medicas"]=medicas
        context["proyectos"]=proyectos

    
        return render(request, 'menor_detalle.html', context)


@login_required      
def menor_actualizar(request, pk, id):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        menor_detalles = get_object_or_404(Menor, id=id)
        form = MenorForm(instance=menor_detalles)
        context={}
        context["pk"]=pk
        context["id"]=id
        context["menor_detalles"]=menor_detalles
        context["beneficiarios"]=beneficiarios
        context["form"]=form
        return render(request, 'menor_actualizar.html', context)
    else:
        try:
            menor_detalles = get_object_or_404(Menor, id=id, user=request.user)
            form = MenorForm(request.POST, instance=menor_detalles)
            act_menor = form.save(commit=False)

            fecha_inicial = act_menor.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)
            
            act_menor.edad = tiempo_transc.years
            act_menor.meses = tiempo_transc.months
            act_menor.user = request.user
            act_menor.save()

            messages.success(request, "Se actualizo satisfactoriamente el Registro")
            return redirect("menor_detalle", pk, id)

        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'menor_actualizar.html', {
            'form': form,
            'pk': pk,
            'id': id
            })


@login_required   
def menor_eliminar(request, pk, id):
    menores = get_object_or_404(Menor, id=id)
    menores.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")
    return redirect('beneficiario_detalle', pk)



# Sesion IMC del Menor

@login_required 
def imc_menor_crear(request, pk, id):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        menor_detalles = get_object_or_404(Menor, id=id)
        proyecto_id = menor_detalles.proyecto_id
        
        form = ImcMenorForm()
        form.fields['jornada'].queryset = Jornada.objects.filter(proyecto=proyecto_id)

        context={}
        context["pk"]=pk
        context["id"]=id
        context["form"]=form
        context["beneficiarios"]=beneficiarios
        context["menor_detalles"]=menor_detalles

        return render(request, 'imc_menor.html', context)

    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            menor_detalles = get_object_or_404(Menor, id=id)
            form = ImcMenorForm(request.POST)
            new_imc_menor = form.save(commit=False)

            xJornada = new_imc_menor.jornada
            xTalla = float(new_imc_menor.talla)
            xPeso = float(new_imc_menor.peso)
            xcbi = float(new_imc_menor.cbi)
            xptr = float(new_imc_menor.ptr)
            xpse = float(new_imc_menor.pse)
            xcc = float(new_imc_menor.cc)

            proyecto = menor_detalles.proyecto
            fecha_inicial = menor_detalles.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)

            xSexo = menor_detalles.sexo
            if xSexo == "MASCULINO":
                xSexo = 1
            else:
                xSexo = 2
            xEdad = tiempo_transc.years
            xMeses = tiempo_transc.months

            xTallaz = xTalla/100
            imc = round(xPeso/(xTallaz**2),2)        

        #***** CLASIFICA POR PESO PARA LA TALLA Y IMC A LOS MENORES DE 5 AÑOS ***

            if xEdad <= 5:
                VtallaI=int(xTalla) 
                residuo = xTalla - VtallaI

                if residuo >= .5:
                    xTallaCal=(VtallaI + .5)
                else: 
                    xTallaCal = VtallaI

                xImc = False

                if ImcPesoTalla_5x.objects.filter(sexo = xSexo, talla = xTallaCal).exists():
                    xImc = ImcPesoTalla_5x.objects.get(sexo = xSexo, talla = xTallaCal)

                if xImc:
                    
                    if xPeso <= xImc.ds3_T:
                        xDiagnostico = 1
                        min_peso = float(xImc.ds3_T) - 1.5
                        max_peso = xImc.ds3_T
                    elif xPeso > xImc.ds3_T and xPeso <= xImc.ds2_T:
                        xDiagnostico = 2 
                        min_peso = xImc.ds3_T
                        max_peso = xImc.ds2_T
                    elif xPeso > xImc.ds2_T and xPeso <= xImc.ds1_T:
                        xDiagnostico = 3
                        min_peso = xImc.ds2_T
                        max_peso = xImc.ds1_T
                    elif xPeso > xImc.ds1_T and xPeso <= xImc.ds1:
                        xDiagnostico = 4
                        min_peso = xImc.ds1_T
                        max_peso = xImc.ds1
                    elif xPeso > xImc.ds1 and xPeso <= xImc.ds2:
                        xDiagnostico = 5
                        min_peso = xImc.ds1
                        max_peso = xImc.ds2
                    elif xPeso > xImc.ds2 and xPeso <= xImc.ds3:
                        xDiagnostico = 6
                        min_peso = xImc.ds2
                        max_peso = xImc.ds3
                    elif xPeso >= xImc.ds3:
                        xDiagnostico = 7
                        min_peso = xImc.ds3
                        max_peso = float(xImc.ds3) + 1.5

        #***** CLASIFICA IMC A LOS MENORES DE 5 AÑOS ***
                    xImc = ImcCla_5x.objects.get(sexo = xSexo, anos = xEdad, meses = xMeses)

                    if imc <= xImc.l3sd:
                        xDiagnostico = 1
                        min_imc = float(xImc.l3sd) - 2
                        max_imc = xImc.l3sd
                    elif imc > xImc.l3sd and imc <= xImc.l2sd:
                        xDiagnostico = 2 
                        min_imc = xImc.l3sd
                        max_imc = xImc.l2sd
                    elif imc > xImc.l2sd and imc <= xImc.l1sd:
                        xDiagnostico = 3
                        min_imc = xImc.l2sd
                        max_imc = xImc.l1sd
                    elif imc > xImc.l1sd and imc <= xImc.sd1:
                        xDiagnostico = 4
                        min_imc = xImc.l1sd
                        max_imc = xImc.sd1
                    elif imc > xImc.sd1 and imc <= xImc.sd2:
                        xDiagnostico = 5
                        min_imc = xImc.sd1
                        max_imc = xImc.sd2
                    elif imc > xImc.sd2 and imc <= xImc.sd3:
                        xDiagnostico = 6
                        min_imc = xImc.sd2
                        max_imc = xImc.sd3
                    elif imc >= xImc.sd3:
                        xDiagnostico = 7
                        min_imc = xImc.sd3
                        max_imc = float(xImc.sd3) + 2


                else:
                    
                    context={}
                    context["pk"]=pk
                    context["id"]=id
                    context["form"]=form
                    context["beneficiarios"]=beneficiarios
                    context["menor_detalles"]=menor_detalles
                    
                    messages.warning(request, "Datos incorectos, Favor verificar la información")
                    return render(request, 'imc_menor.html', context)
                

        #***** CLASIFICA POR IMC A LOS MAYORES DE 5 AÑOS Y MENORES DE 19 AÑOS ***
            elif xEdad > 5 and xEdad < 19:
                min_imc = 0
                max_imc = 0
                xImc = False

                if ImcCla.objects.filter(sexo = xSexo, anos = xEdad, meses = xMeses).exists():
                    xImc = ImcCla.objects.get(sexo = xSexo, anos = xEdad, meses = xMeses)
                
                if xImc:
                    if imc <= xImc.l3sd:
                        xDiagnostico = 1
                        min_peso = float(xImc.l3sd) - 2
                        max_peso = xImc.l3sd
                    elif imc > xImc.l3sd and imc <= xImc.l2sd:
                        xDiagnostico = 2 
                        min_peso = xImc.l3sd
                        max_peso = xImc.l2sd
                    elif imc > xImc.l2sd and imc <= xImc.l1sd:
                        xDiagnostico = 3
                        min_peso = xImc.l2sd
                        max_peso = xImc.l1sd
                    elif imc > xImc.l1sd and imc <= xImc.sd1:
                        xDiagnostico = 4
                        min_peso = xImc.l1sd
                        max_peso = xImc.sd1
                    elif imc > xImc.sd1 and imc <= xImc.sd2:
                        xDiagnostico = 5
                        min_peso = xImc.sd1
                        max_peso = xImc.sd2
                    elif imc > xImc.sd2 and imc <= xImc.sd3:
                        xDiagnostico = 6
                        min_peso = xImc.sd2
                        max_peso = xImc.sd3
                    elif imc >= xImc.sd3:
                        xDiagnostico = 7
                        min_peso = xImc.sd3
                        max_peso = float(xImc.sd3) + 2
                else:
                    print(xEdad)
                    context={}
                    context["pk"]=pk
                    context["id"]=id
                    context["form"]=form
                    context["beneficiarios"]=beneficiarios
                    context["menor_detalles"]=menor_detalles
                    messages.warning(request, "Datos incorectos, Favor verificar la información")
                    return render(request, 'imc_menor.html', context)

        
        #***** CLASIFICA DE IMC A LOS MAYORES DE 19 AÑOS ***
            elif xEdad >= 19:
                xDiagTalla = 26
                min_talla = 0
                max_talla = 0
                min_imc = 0
                max_imc = 0
                min_peso = 0
                max_peso = 0
            
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


            if xEdad < 19:
                xImcTalla = ImcTalla.objects.get(sexo = xSexo, anos = xEdad, meses = xMeses)
                if xTalla <= xImcTalla.sd2_T:
                    xDiagTalla = 21
                    min_talla = float(xImcTalla.sd2_T) - 2
                    max_talla = xImcTalla.sd2_T
                elif xTalla > xImcTalla.sd2_T and xTalla <= xImcTalla.sd1_T:
                    xDiagTalla = 22
                    min_talla = xImcTalla.sd2_T
                    max_talla = xImcTalla.sd1_T
                elif xTalla > xImcTalla.sd1_T and xTalla <= xImcTalla.sd1:
                    xDiagTalla = 23
                    min_talla = xImcTalla.sd1_T
                    max_talla = xImcTalla.sd1
                elif xTalla > xImcTalla.sd1 and xTalla <= xImcTalla.sd2:
                    xDiagTalla = 24
                    min_talla = xImcTalla.sd1
                    max_talla = xImcTalla.sd2
                elif xTalla >= xImcTalla.sd2:
                    xDiagTalla = 25
                    min_talla = xImcTalla.sd2
                    max_talla = float(xImcTalla.sd2) + 2


        #********   DIAGNOSTICO   **********

            xDiag = Diagnostico.objects.get(codigo_diag = xDiagnostico)
            diag_peso = xDiag.diagnostico

            xDiagTallas = Diagnostico.objects.get(codigo_diag = xDiagTalla)
            diag_talla = xDiagTallas.diagnostico

        #********   SALVAR   **********

            imc_menor = AntropMenor(cedula_bef_id=pk, cedula_id = id, proyecto = proyecto, jornada = xJornada, edad = xEdad, meses = xMeses, peso = xPeso, talla = xTalla, cbi = xcbi, ptr = xptr, pse = xpse, cc = xcc, imc = imc, diagnostico = diag_peso, diagnostico_talla = diag_talla, min_peso = min_peso, max_peso = max_peso, min_talla = min_talla, max_talla = max_talla,min_imc = min_imc, max_imc = max_imc)
                
            imc_menor.save()
            idimc=imc_menor.id

            menor_detalles.edad = tiempo_transc.years
            menor_detalles.meses = tiempo_transc.months
            menor_detalles.peso_actual = xPeso
            menor_detalles.talla_actual = xTalla
            menor_detalles.cbi_actual = xcbi
            menor_detalles.imc_actual = imc
            menor_detalles.pse_actual = xpse
            menor_detalles.ptr_actual = xptr
            menor_detalles.cc_actual = xcc
            menor_detalles.diagnostico_actual = diag_peso
            menor_detalles.diagnostico_talla_actual = diag_talla
            menor_detalles.save()

            return redirect("imc_menor_riesgo", pk, id, idimc)
        
        except ValueError:

            context={}
            context["pk"]=pk
            context["id"]=id
            context["form"]=form
            context["beneficiarios"]=beneficiarios
            context["menor_detalles"]=menor_detalles
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'imc_menor.html', context)


@login_required     
def imc_menor_riesgo(request, pk, id, idimc):
        
    if request.method == 'GET':

        menor_detalles = get_object_or_404(Menor, id=id)
        imc_menores = get_object_or_404(AntropMenor, id=idimc)
        diag_peso = get_object_or_404(Diagnostico, diagnostico = imc_menores.diagnostico)
        diag_talla = get_object_or_404(Diagnostico, diagnostico = imc_menores.diagnostico_talla)
        if menor_detalles.edad <= 5:
            peso = str(imc_menores.peso).replace(',','.')
        else:
            peso = str(imc_menores.imc).replace(',','.')
        talla = str(imc_menores.talla).replace(',','.')
        imc = str(imc_menores.imc).replace(',','.')
        min_peso = str(imc_menores.min_peso).replace(',','.')
        max_peso = str(imc_menores.max_peso).replace(',','.')
        min_talla = str(imc_menores.min_talla).replace(',','.')
        max_talla = str(imc_menores.max_talla).replace(',','.')
        min_imc = str(imc_menores.min_imc).replace(',','.')
        max_imc = str(imc_menores.max_imc).replace(',','.')

        context = {}
        context["pk"]=pk
        context["id"]=id
        context["menor_detalles"]=menor_detalles
        context["idimc"]=idimc
        context["peso"]=peso
        context["talla"]=talla
        context["imc"]=imc
        context["min_peso"]=min_peso
        context["max_peso"]=max_peso
        context["min_talla"]=min_talla
        context["max_talla"]=max_talla
        context["min_imc"]=min_imc
        context["max_imc"]=max_imc
        context["diag_peso"]=diag_peso
        context["diag_talla"]=diag_talla
        context["imc_menores"]=imc_menores

        return render(request, "imc_menor_riesgo.html", context)   

    if request.method=="POST":
        try:
            xriesgo = request.POST.get("riesgo")
            xservicio = request.POST.get("servicio")
            xcentro_hospital = request.POST.get("centro_hospital")
            xobservacion = request.POST.get("observacion")
        
            riesgos = get_object_or_404(AntropMenor, id=idimc)
            riesgos.riesgo=xriesgo
            riesgos.servicio=xservicio
            riesgos.centro_hospital=xcentro_hospital
            riesgos.observacion=xobservacion       
    
            riesgos.save()
            messages.success(request, "Se guardo satisfactoriamente el Registro")
            return redirect( "menor_detalle", pk, id)
        
        except ValueError:
            menor_detalles = get_object_or_404(Menor, id=id)
            imc_menores = get_object_or_404(AntropMenor, id=idimc)
            diagnosticos = get_object_or_404(Diagnostico, diagnostico=imc_menores.diagnostico)
            context = {}
            context["pk"]=pk
            context["id"]=id
            context["menor_detalles"]=menor_detalles
            context["idimc"]=idimc
            context["imc_menores"]=imc_menores
            context["diagnosticos"]=diagnosticos

            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'imc_menor_riesgo.html', context)
    

@login_required 
def imc_menor_detalle(request, pk, id, idimc):

    if request.method == 'GET':

        menor_detalles = get_object_or_404(Menor, id=id)
        imc_menores = get_object_or_404(AntropMenor, id=idimc)
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        diag_peso = get_object_or_404(Diagnostico, diagnostico = imc_menores.diagnostico)
        diag_talla = get_object_or_404(Diagnostico, diagnostico = imc_menores.diagnostico_talla)
        if menor_detalles.edad <= 5:
            peso = str(imc_menores.peso).replace(',','.')
        else:
            peso = str(imc_menores.imc).replace(',','.')

        talla = str(imc_menores.talla).replace(',','.')
        imc = str(imc_menores.imc).replace(',','.')
        min_peso = str(imc_menores.min_peso).replace(',','.')
        max_peso = str(imc_menores.max_peso).replace(',','.')
        min_talla = str(imc_menores.min_talla).replace(',','.')
        max_talla = str(imc_menores.max_talla).replace(',','.')
        min_imc = str(imc_menores.min_imc).replace(',','.')
        max_imc = str(imc_menores.max_imc).replace(',','.')

        context = {}
        context["pk"]=pk
        context["idimc"]=id
        context["idimc"]=idimc
        context["peso"]=peso
        context["talla"]=talla
        context["imc"]=imc
        context["min_peso"]=min_peso
        context["max_peso"]=max_peso
        context["min_talla"]=min_talla
        context["max_talla"]=max_talla
        context["min_imc"]=min_imc
        context["max_imc"]=max_imc
        context["menor_detalles"]=menor_detalles
        context["imc_menores"]=imc_menores
        context["diag_peso"]=diag_peso
        context["diag_talla"]=diag_talla
        context["beneficiarios"]=beneficiarios

        return render(request, "imc_menor_detalle.html", context)   


@login_required   
def imc_menor_eliminar(request, pk, id, idimc):
    imc_menores = get_object_or_404(AntropMenor, id=idimc)
    imc_menores.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")
    return redirect( "menor_detalle", pk, id)


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



# Sesion de Medica 

@login_required  
def medica_crear(request, pk, id):
    if request.method == 'GET':
        beneficiarios = get_object_or_404(Beneficiario, id=pk)
        menor_detalles = get_object_or_404(Menor, id=id)
        
        proyecto_id = menor_detalles.proyecto_id
        form = MedicaForm()
        form.fields['jornada'].queryset = Jornada.objects.filter(proyecto=proyecto_id)

        context={}
        context["pk"]=pk
        context["id"]=id
        context["beneficiarios"]=beneficiarios
        context["menor_detalles"]=menor_detalles
        context["form"]=form
        return render(request, 'medica_crear.html', context)
    else:
        try:
            beneficiarios = get_object_or_404(Beneficiario, id=pk)
            menor_detalles = get_object_or_404(Menor, id=id)
            form = MedicaForm(request.POST)
            fecha_inicial = menor_detalles.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)
            new_medica = form.save(commit=False)
            new_medica.cedula_bef_id = pk
            new_medica.cedula_id = id
            new_medica.proyecto = menor_detalles.proyecto
            new_medica.fecha = dia_hoy
            new_medica.edad = tiempo_transc.years
            new_medica.meses = tiempo_transc.months
            new_medica.save()
            menor_detalles.edad = tiempo_transc.years
            menor_detalles.meses = tiempo_transc.months
            menor_detalles.save()

            messages.success(request, "Se guardo satisfactoriamente el Registro")
            return redirect( "menor_detalle", pk, id)

        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'medica_crear.html', {
            'pk': pk,
            'id':id,
            'form': form,
            'bemeficiarios':beneficiarios,
            'menor_detalles':menor_detalles,
            })


@login_required      
def medica_detalle(request, pk, id, idmed):
    if request.method == 'GET':

        medicas = get_object_or_404(Medica, id=idmed)
        form = MedicaForm(instance=medicas)

        beneficiarios = get_object_or_404(Beneficiario,id=pk)
        menor_detalles = get_object_or_404(Menor,id=id)
        context={}
        context["pk"]=pk
        context["id"]=id
        context["idmed"]=idmed
        context["form"]=form
        context["beneficiarios"]=beneficiarios
        context["menor_detalles"]=menor_detalles
        context["medicas"]=medicas
    
        return render(request, 'medica_detalle.html', context)
    else:
        try:
            medicas = get_object_or_404(Medica, id=idmed)
            form = MedicaForm(request.POST, instance=medicas)
            new_medica = form.save(commit=False)
            menor_detalles = get_object_or_404(Menor, id=id)
            fecha_inicial = menor_detalles.fecha_nac
            dia_hoy = date.today()
            fecha_fin = dia_hoy.strftime('%d-%m-%Y')
            fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
            tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)

            new_medica.edad = tiempo_transc.years
            new_medica.meses = tiempo_transc.months
            new_medica.save()

            menor_detalles.edad = tiempo_transc.years
            menor_detalles.meses = tiempo_transc.months
            menor_detalles.save()

            messages.success(request, "Se actualizo satisfactoriamente el Registro")
            return redirect("menor_detalle", pk, id)
        
        except ValueError:
            messages.warning(request, "Datos incorectos, Favor verificar la información")
            return render(request, 'medica_detalle.html', {
            'form': form,
            'pk': pk,
            'id': id
            })


@login_required   
def medica_eliminar(request, pk, id, idmed):
    medicas = get_object_or_404(Medica, id=idmed)
    medicas.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")

    return redirect("menor_detalle", pk, id)


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


