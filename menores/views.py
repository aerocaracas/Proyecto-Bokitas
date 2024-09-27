from django.shortcuts import render, redirect, get_object_or_404
from bokitas.models import Menor, Beneficiario, AntropMenor, Medica, Proyecto,Jornada
from bokitas.models import ImcCla, ImcPesoTalla_5x, ImcTalla, ImcCla_5x, Diagnostico
from menores.forms import MenorForm, ImcMenorForm, MedicaForm
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from beneficiario.forms import ExpProyectoForm
from django.core.paginator import Paginator
from datetime import datetime, date
from dateutil import relativedelta
from django.contrib import messages



# Sesion Menores.
@login_required  
def menores(request):

    menores = Menor.objects.all()
    proyect = ExpProyectoForm
    query = ""
    page = request.GET.get('page',1)

    try:
        if "search" in request.POST:
            query = request.POST.get("searchquery")
            menores = Menor.objects.filter(Q(cedula__icontains=query) | Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(proyecto__proyecto__icontains=query) | Q(cedula_bef__cedula__contains=query))
        paginator = Paginator(menores, 15)
        menores = paginator.page(page)
    except:
        messages.warning(request, "No hay Menores registrados o Datos incorectos, Favor verificar la información")
        return redirect('menores')
    
    return render(request, 'menores.html',{
        'entity': menores,
        'query': query,
        'proyect':proyect,
        'paginator': paginator
    })


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

            if menor_detalles.peso_inicial == 0:
                menor_detalles.peso_inicial = xPeso
                menor_detalles.talla_inicial = xTalla
                menor_detalles.cbi_inicial = xcbi
                menor_detalles.imc_inicial = imc
                menor_detalles.pse_inicial = xpse
                menor_detalles.ptr_inicial = xptr
                menor_detalles.cc_inicial = xcc
                menor_detalles.diagnostico_inicial = diag_peso
                menor_detalles.diagnostico_talla_inicial = diag_talla

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
            'id': id,
            'idmed': idmed,
            })


@login_required   
def medica_eliminar(request, pk, id, idmed):
    medicas = get_object_or_404(Medica, id=idmed)
    medicas.delete()
    messages.error(request, "Se Elimino satisfactoriamente el registro")

    return redirect("menor_detalle", pk, id)

