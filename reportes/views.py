from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bokitas.models import Proyecto, Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica, Nutricional
from django.db.models import Q
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference

# Create your views here.

class exportar_proyecto(TemplateView):
    def get(self, request, *args, **kwargs):
        proyecto = request.GET.get('proyecto')
        workbook = Workbook()
        bandera = True
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m')
        
        hojas = ["REGISTRO BENEFICIARIOS","REGISTRO MENORES","ANTROPOMETRICOS MENORES","ANTROPOMETRICO EMBARAZADAS","ANTROPOMETRICO LACTANTE","MEDICAMENTOS Y PRODUCTOS"]

        for hoja in hojas: 
            if bandera:
                worksheet = workbook.active
                worksheet.title = hoja
                bandera = False
                worksheet.merge_cells('A1:C1')
                first_cell = worksheet['A1']
                first_cell.value = "Fecha: " + fecha_fin
            else:
                worksheet = workbook.create_sheet(hoja)

    #*********  Crear encabezado en la hoja  *************
            worksheet.merge_cells('A2:D2')
            second_cell = worksheet['A2']
            second_cell.value = "Bokitas"
            second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")

            worksheet.merge_cells('A3:D3')
            third_cell = worksheet['A3']
            third_cell.value = "Bokitas Fundation    www.bokitas.org"
            third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  HOJA DE DATOS DE LOS BENEFICIARIOS  ********************************

    #*********  Registro de Datos de los Beneficiario  *************
        worksheet = workbook.worksheets[0]
        worksheet.merge_cells('A4:W6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DE LOS BENEFICIARIOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        beneficiarios = Beneficiario.objects.filter(proyecto=proyecto).order_by('cedula')
        
        #**************  Obtener el total de beneficiarios  ***************

        total_beneficiarios = beneficiarios.count()
        total_embarazadas = beneficiarios.values("embarazada").filter(embarazada="SI").count()
        total_lactantes = beneficiarios.values("lactante").filter(lactante="SI").count()


        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','NACIONALIDAD','NUM HIJOS','EMBARAZADA','LACTANDO','ESTADO CIVIL','EDUCACIÓN','PROFESIÓN','LABORAL','TELEFONO','CORREO','DIRECCIÓN','CIUDAD','ESTADO','ESTATUS','NÚMERO DE CUENTA']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        for beneficiario in beneficiarios:
            row_num += 1
            if beneficiario.fecha_nac:
                datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac.strftime('%d-%m-%Y'),beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]
            else:
                datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac,beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]


            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 6 or col_num == 7 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 22:
                    cell.alignment = Alignment(horizontal="center")

        #**************  Agrega el total de beneficiarios  ************************
        row_num += 2
        worksheet.merge_cells('A'+str(row_num+1)+':B'+str(row_num+1))
        cell = worksheet.cell(row=row_num+1, column=1)
        cell.value = "Total de Beneficiarios: " +' ' + str(total_beneficiarios)
        cell2 = worksheet.cell(row=row_num+2, column=1)
        cell2.value = "Total de Embarazadas: " +' ' + str(total_embarazadas)
        cell3 = worksheet.cell(row=row_num+3, column=1)
        cell3.value = "Total de Lactantes: " +' ' + str(total_lactantes)

#***********************  HOJA DE DATOS DE LOS MENORES  ********************************

    #*********  Registro de Datos de los Menores  *************
        worksheet = workbook.worksheets[1]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTROS DEL PERFIL DE MENORES"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        menores = Menor.objects.filter(proyecto=proyecto).order_by('-cedula_bef')

        #**************  Obtener el total de Menores  ***************
        total_menores = menores.count()
        total_activos = menores.values("estatus").filter(estatus="ACTIVO").count()
        total_altas = menores.values("estatus").filter(estatus="ALTA").count()
        total_egresos = menores.values("estatus").filter(estatus="EGRESO").count()
        total_desincorporados = menores.values("estatus").filter(estatus="DESINCORPORADO").count()
        total_menores_5 = menores.values("edad").filter(edad__lte=5).count()
        total_menores_2 = menores.values("edad").filter(edad__lte=2).count()

        titulos = ['PROYECTO','REPRESENTANTE','PARENTESCO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','DIAGNOSTICO PESO','DIAGNOSTICO TALLA','FECHA INGRESO','ESTATUS']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        for menor in menores:
            row_num += 1
            datos = [menor.proyecto,menor.cedula_bef,menor.parentesco,menor.cedula,menor.nombre,menor.apellido,menor.sexo,menor.fecha_nac.strftime('%d-%m-%Y'),menor.edad,menor.meses,menor.peso_actual,menor.talla_actual,menor.diagnostico_actual,menor.diagnostico_talla_actual,menor.fecha_ing_proyecto.strftime('%d-%m-%Y'),menor.estatus]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 3 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 15 or col_num == 16:
                    cell.alignment = Alignment(horizontal="center")

        #**************  Agrega el total de Menores  ************************
        row_num += 2
        worksheet.merge_cells('A'+str(row_num+1)+':B'+str(row_num+1))
        cell = worksheet.cell(row=row_num+1, column=1)
        cell.value = "Total de Menores: " +' ' + str(total_menores)
        cell2 = worksheet.cell(row=row_num+2, column=1)
        cell2.value = "Total de Activos: " +' ' + str(total_activos)
        cell3 = worksheet.cell(row=row_num+3, column=1)
        cell3.value = "Total de Altas: " +' ' + str(total_altas)
        cell4 = worksheet.cell(row=row_num+4, column=1)
        cell4.value = "Total de Egresos: " +' ' + str(total_egresos)
        cell5 = worksheet.cell(row=row_num+5, column=1)
        cell5.value = "Total de Desincorporados: " +' ' + str(total_desincorporados)
        cell6 = worksheet.cell(row=row_num+6, column=1)
        cell6.value = "Total de Menores de 5 años: " +' ' + str(total_menores_5)
        cell7 = worksheet.cell(row=row_num+7, column=1)
        cell7.value = "Total de Menores de 2 años: " +' ' + str(total_menores_2)


#*************  HOJA DE DATOS ANTROPOMETRICOS DEL MENORES  *********************

    #*********  Registro de Datos antropometricos Menores  *************
        worksheet = workbook.worksheets[2]
        worksheet.merge_cells('A4:W6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DATOS ANTROPOMETRICOS DEL MENOR"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_menores = AntropMenor.objects.filter(proyecto_id=proyecto).order_by('-cedula_bef','cedula_id').select_related('cedula')

        titulos = ['PROYECTO','REPRESENTANTE','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','FECHA JORNADA','EDAD','MESES','PESO','TALLA','CBI','PTR','PSE','CC','IMC','DIAGNOSTICO PESO','DIAGNOSTICO TALLA']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_menores:
            row_num += 1
            datos = [imc.proyecto,imc.cedula_bef,imc.cedula.cedula,imc.cedula.nombre,imc.cedula.apellido,imc.cedula.sexo,imc.cedula.fecha_nac.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.cedula.peso_actual,imc.cedula.talla_actual,imc.jornada.jornada.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.peso,imc.talla,imc.cbi,imc.ptr,imc.pse,imc.cc,imc.imc,imc.diagnostico,imc.diagnostico_talla]

            if imc.cedula.cedula != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="center")
                    if col_num == 1 or col_num == 2 or col_num == 4 or col_num == 5 or col_num == 22 or col_num == 23:
                        cell.alignment = Alignment(horizontal="left")

                xCedula = imc.cedula.cedula
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 11:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")
                        if col_num == 22 or col_num == 23:
                            cell.alignment = Alignment(horizontal="left")


#*************  HOJA DE DATOS ANTROPOMETRICOS EMBARAZADAS  *********************

    #*********  Registro de Datos antropometricos Embarazadas  *************
        worksheet = workbook.worksheets[3]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DATOS ANTROPOMETRICOS EMBARAZADAS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_embarazos = AntropBef.objects.filter(proyecto=proyecto, embarazo_lactando = 'EMBARAZADA').order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA NAC.','FECHA JORNADA','EDAD','MESES','MESES EMBARAZO','PESO','TALLA','CBI','IMC','DIAGNOSTICO PESO','RIESGO','OBSERVACIONES']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_embarazos:
            row_num += 1
            if beneficiario.fecha_nac:
                datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac.strftime('%d-%m-%Y'),imc.jornada.jornada.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]
            else:
                datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac,imc.jornada.jornada.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]

            if imc.cedula_bef.cedula != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="center")
                    if col_num == 1 or col_num == 2 or col_num == 3 or col_num == 4:
                        cell.alignment = Alignment(horizontal="left")

                xCedula = imc.cedula_bef.cedula
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 7:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")


#*************  HOJA DE DATOS ANTROPOMETRICOS LACTANTES  *********************

    #*********  Registro de Datos antropometricos Lactante  *************
        worksheet = workbook.worksheets[4]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DATOS ANTROPOMETRICOS LACTANTES"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_embarazos = AntropBef.objects.filter(proyecto=proyecto, embarazo_lactando = 'LACTANDO').order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA NAC.','FECHA JORNADA','EDAD','MESES','MESES LACTANDO','PESO','TALLA','CBI','IMC','DIAGNOSTICO PESO','RIESGO','OBSERVACIONES']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_embarazos:
            row_num += 1
            if beneficiario.fecha_nac:
                datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac.strftime('%d-%m-%Y'),imc.jornada.jornada.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]
            else:
                datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac,imc.jornada.jornada.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]

            if imc.cedula_bef.cedula != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="center")
                    if col_num == 1 or col_num == 2 or col_num == 3 or col_num == 4:
                        cell.alignment = Alignment(horizontal="left")

                xCedula = imc.cedula_bef.cedula
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 7:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")

#*************  HOJA DE DATOS ENTREGA MEDICAMENTOS PRODUCTOS  *********************

    #*********  Registro de Datos DATOS ENTREGA MEDICAMENTOS  *************
        worksheet = workbook.worksheets[5]
        worksheet.merge_cells('A4:H6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DE ENTREGA DE MEDICAMENTOS Y PRODUCTOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        medicamentos = Medicamento.objects.filter(proyecto=proyecto).order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA JORNADA','NOMBRE DEL PRODUCTO','DESCRIPCION DEL PRODUCTO','CANTIDAD']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas

        for med in medicamentos:
            row_num += 1
            datos = [med.cedula_bef.proyecto,med.cedula_bef.cedula,med.cedula_bef.nombre,med.cedula_bef.apellido,med.jornada,med.nombre,med.descripcion,med.cantidad]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                cell.alignment = Alignment(horizontal="center")
                if col_num == 1 or col_num == 2 or col_num == 3 or col_num == 4:
                    cell.alignment = Alignment(horizontal="left")


    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_por_Proyecto.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    


class exp_beneficiario_detalle(TemplateView):
    def get(self, request,  pk, *args, **kwargs):
        workbook = Workbook()
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m') 
        worksheet = workbook.active
        worksheet.title = "REGISTRO BENEFICIARIO"
        worksheet.merge_cells('A1:C1')
        first_cell = worksheet['A1']
        first_cell.value = "Fecha: " + fecha_fin

    #*********  Crear encabezado en la hoja  *************
        worksheet.merge_cells('A2:D2')
        second_cell = worksheet['A2']
        second_cell.value = "Bokitas"
        second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")

        worksheet.merge_cells('A3:D3')
        third_cell = worksheet['A3']
        third_cell.value = "Bokitas Fundation    www.bokitas.org"
        third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  HOJA DE DATOS DE LOS BENEFICIARIOS  ********************************

    #*********  Registro de Datos de los Beneficiario  *************
        worksheet = workbook.worksheets[0]
       # worksheet = workbook['REGISTRO BENEFICIARIOS']
        worksheet.merge_cells('A4:W6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DEL BENEFICIARIO"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        beneficiarios = Beneficiario.objects.filter(id=pk)
        
        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','NACIONALIDAD','NUM HIJOS','EMBARAZADA','LACTANDO','ESTADO CIVIL','EDUCACIÓN','PROFESIÓN','LABORAL','TELEFONO','CORREO','DIRECCIÓN','CIUDAD','ESTADO','ESTATUS','NÚMERO DE CUENTA']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        for beneficiario in beneficiarios:
            row_num += 1
            if beneficiario.fecha_nac:
                datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac.strftime('%d-%m-%Y'),beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]
            else:
                datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac,beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 6 or col_num == 7 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 22:
                    cell.alignment = Alignment(horizontal="center")


    
    #*********  Registro de Datos antropometricos Menores  *************

        row_num = row_num + 3
        xx = 'A'+ str(row_num)
        yy = 'V'+ str(row_num + 2)
        worksheet.merge_cells(xx +':'+ yy)
        fourth_cell = worksheet[xx]
        fourth_cell.value = "REGISTRO DE HIJOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_menores = AntropMenor.objects.filter(cedula_bef_id = pk).order_by('cedula_id').select_related('cedula')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','FECHA JORNADA','EDAD','MESES','PESO','TALLA','CBI','PTR','PSE','CC','IMC','DIAGNOSTICO PESO','DIAGNOSTICO TALLA']
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")
        row_num = row_num + 3
    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            if col_num > 10:
                cell.fill = PatternFill("solid", fgColor="9EEAF9")
            else:
                cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if col_num == 21 or col_num == 22: 
                adjusted_width = (len(cell.value) + 10) * 1.2
                worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_menores:
            row_num += 1
            datos = [imc.proyecto,imc.cedula.cedula,imc.cedula.nombre,imc.cedula.apellido,imc.cedula.sexo,imc.cedula.fecha_nac.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.cedula.peso_actual,imc.cedula.talla_actual,imc.jornada.jornada.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.peso,imc.talla,imc.cbi,imc.ptr,imc.pse,imc.cc,imc.imc,imc.diagnostico,imc.diagnostico_talla]
            
            if imc.cedula.cedula != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=double, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="center")
                    if col_num == 1 or col_num == 2 or col_num == 3 or col_num == 4 or col_num == 5 or col_num == 21 or col_num == 22:
                        cell.alignment = Alignment(horizontal="left")

                xCedula = imc.cedula.cedula
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 10:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")
                        if col_num == 21 or col_num == 22:
                            cell.alignment = Alignment(horizontal="left")


    #*********  Registro de Datos antropometricos Beneficiario *************
    
        row_num = row_num + 3
        xx = 'A'+ str(row_num)
        yy = 'O'+ str(row_num + 2)
        worksheet.merge_cells(xx +':'+ yy)
        fourth_cell = worksheet[xx]
        fourth_cell.value = "REGISTRO ANTROPOMÉTRICO DEL BENEFICIARIO"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_beneficiario = AntropBef.objects.filter(cedula_bef_id = pk).order_by('cedula_bef_id').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','FECHA JORNADA','ESTADO','EDAD','MESES','PESO','TALLA','CBI','IMC','DIAGNOSTICO PESO']
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")
        row_num = row_num + 3
    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            if col_num > 6:
                cell.fill = PatternFill("solid", fgColor="9EEAF9")
            else:
                cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if col_num == 21 or col_num == 22: 
                adjusted_width = (len(cell.value) + 10) * 1.2
                worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_beneficiario:
            row_num += 1
            datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.sexo,imc.cedula_bef.fecha_nac.strftime('%d-%m-%Y'),imc.jornada.jornada.strftime('%d-%m-%Y'),imc.embarazo_lactando,imc.edad,imc.meses,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico]
            
            if imc.cedula_bef != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="left")
                    if col_num == 6 or col_num == 7 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 13 or col_num == 14:
                        cell.alignment = Alignment(horizontal="center")

                xCedula = imc.cedula_bef
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 6:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")
                        if col_num == 15:
                            cell.alignment = Alignment(horizontal="left")


    #*********  Registro entrega de Medicamentos / Productos al Beneficiario *************
    
        row_num = row_num + 3
        xx = 'A'+ str(row_num)
        yy = 'H'+ str(row_num + 2)
        worksheet.merge_cells(xx +':'+ yy)
        fourth_cell = worksheet[xx]
        fourth_cell.value = "REGISTRO DE ENTREGA DE MEDICAMENTOS / PRODUCTOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        medicamentos = Medicamento.objects.filter(cedula_bef_id = pk).order_by('cedula_bef_id').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA JORNADA','NOMBRE PROD.',' DESCRIPCIÓN ','CANTIDAD']
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")
        row_num = row_num + 3
    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if col_num == 5 or col_num == 7: 
                adjusted_width = (len(cell.value) + 10) * 1.2
                worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for med in medicamentos:
            row_num += 1
            datos = [med.cedula_bef.proyecto,med.cedula_bef.cedula,med.cedula_bef.nombre,med.cedula_bef.apellido,med.jornada.jornada.strftime('%d-%m-%Y'),med.nombre,med.descripcion,med.cantidad]
            
            
            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                cell.alignment = Alignment(horizontal="left")
                if col_num == 5 or col_num == 8:
                    cell.alignment = Alignment(horizontal="center")



    #*********  Registro Familiares del Beneficiario *************
    
        row_num = row_num + 3
        xx = 'A'+ str(row_num)
        yy = 'L'+ str(row_num + 2)
        worksheet.merge_cells(xx +':'+ yy)
        fourth_cell = worksheet[xx]
        fourth_cell.value = "REGISTRO DE FAMILIARES DEL BENEFICIARIO"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        familiares = Familia.objects.filter(cedula_bef_id = pk)

        titulos = ['PARENTESCO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','ESTADO CIVIL',' EDUCACIÓN ','PROFESIÓN','LABORAL']
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")
        row_num = row_num + 3
    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if col_num == 5 or col_num == 7: 
                adjusted_width = (len(cell.value) + 10) * 1.2
                worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for fam in familiares:
            row_num += 1
            datos = [fam.parentesco,fam.cedula,fam.nombre,fam.apellido,fam.sexo,fam.fecha_nac.strftime('%d-%m-%Y'),fam.edad,fam.meses,fam.estado_civil,fam.educacion,fam.profesion,fam.laboral]
            
            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                cell.alignment = Alignment(horizontal="left")
                if col_num == 6 or col_num == 7 or col_num == 8:
                    cell.alignment = Alignment(horizontal="center")


    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Rep_Beneficiario_detalle.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    


class listado_beneficiario(TemplateView):
    def get(self, request, *args, **kwargs):
        proyecto = request.GET.get('proyecto')
        workbook = Workbook()
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m') 
        worksheet = workbook.active
        worksheet.title = "LISTADO DE BENEFICIARIOS"
        worksheet.merge_cells('A1:C1')
        first_cell = worksheet['A1']
        first_cell.value = "Fecha: " + fecha_fin

    #*********  Crear encabezado en la hoja  *************
        worksheet.merge_cells('A2:D2')
        second_cell = worksheet['A2']
        second_cell.value = "Bokitas"
        second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")

        worksheet.merge_cells('A3:D3')
        third_cell = worksheet['A3']
        third_cell.value = "Bokitas Fundation    www.bokitas.org"
        third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  HOJA DE DATOS DE LOS BENEFICIARIOS  ********************************

    #*********  Registro de Datos de los Beneficiario  *************
        
        worksheet = workbook.worksheets[0]
        worksheet.merge_cells('A4:W6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DEL BENEFICIARIO"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center") 

        beneficiarios = Beneficiario.objects.filter(proyecto=proyecto)

        #**************  Obtener el total de beneficiarios  ***************
        total_beneficiarios = beneficiarios.count()
        total_embarazadas = beneficiarios.values("embarazada").filter(embarazada="SI").count()
        total_lactantes = beneficiarios.values("lactante").filter(lactante="SI").count()

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','NACIONALIDAD','NUM HIJOS','EMBARAZADA','LACTANDO','ESTADO CIVIL','EDUCACIÓN','PROFESIÓN','LABORAL','TELEFONO','CORREO','DIRECCIÓN','CIUDAD','ESTADO','ESTATUS','NÚMERO DE CUENTA']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        for beneficiario in beneficiarios:
            row_num += 1
            if beneficiario.fecha_nac:
                datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac.strftime('%d-%m-%Y'),beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]
            else:
                datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac,beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 6 or col_num == 7 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 22:
                    cell.alignment = Alignment(horizontal="center")

        #**************  Agrega el total de beneficiarios  ************************
        row_num += 2
        worksheet.merge_cells('A'+str(row_num+1)+':B'+str(row_num+1))
        cell = worksheet.cell(row=row_num+1, column=1)
        cell.value = "Total de Beneficiarios: " +' ' + str(total_beneficiarios)
        cell2 = worksheet.cell(row=row_num+2, column=1)
        cell2.value = "Total de Embarazadas: " +' ' + str(total_embarazadas)
        cell3 = worksheet.cell(row=row_num+3, column=1)
        cell3.value = "Total de Lactantes: " +' ' + str(total_lactantes)


    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Rep_listado_Beneficiarios.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    


class listado_menores(TemplateView):
    def get(self, request, *args, **kwargs):
        proyecto = request.GET.get('proyecto')
        workbook = Workbook()
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m') 
        worksheet = workbook.active
        worksheet.title = "LISTADO DE MENORES"
        worksheet.merge_cells('A1:C1')
        first_cell = worksheet['A1']
        first_cell.value = "Fecha: " + fecha_fin

    #*********  Crear encabezado en la hoja  *************
        worksheet.merge_cells('A2:D2')
        second_cell = worksheet['A2']
        second_cell.value = "Bokitas"
        second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")

        worksheet.merge_cells('A3:D3')
        third_cell = worksheet['A3']
        third_cell.value = "Bokitas Fundation    www.bokitas.org"
        third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  HOJA DE DATOS DE LOS MENORES  ********************************

    #*********  Registro de Datos de los Menores  *************
        worksheet = workbook.worksheets[0]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTROS DEL PERFIL DE MENORES"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        menores = Menor.objects.filter(proyecto=proyecto).order_by('-cedula_bef')

        #**************  Obtener el total de Menores  ***************
        total_menores = menores.count()
        total_activos = menores.values("estatus").filter(estatus="ACTIVO").count()
        total_altas = menores.values("estatus").filter(estatus="ALTA").count()
        total_egresos = menores.values("estatus").filter(estatus="EGRESO").count()
        total_desincorporados = menores.values("estatus").filter(estatus="DESINCORPORADO").count()
        total_menores_5 = menores.values("edad").filter(edad__lte=5).count()
        total_menores_2 = menores.values("edad").filter(edad__lte=2).count()

        titulos = ['PROYECTO','REPRESENTANTE','PARENTESCO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','DIAGNOSTICO PESO','DIAGNOSTICO TALLA','FECHA INGRESO','ESTATUS']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        for menor in menores:
            row_num += 1
            datos = [menor.proyecto,menor.cedula_bef,menor.parentesco,menor.cedula,menor.nombre,menor.apellido,menor.sexo,menor.fecha_nac.strftime('%d-%m-%Y'),menor.edad,menor.meses,menor.peso_actual,menor.talla_actual,menor.diagnostico_actual,menor.diagnostico_talla_actual,menor.fecha_ing_proyecto.strftime('%d-%m-%Y'),menor.estatus]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 3 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 15 or col_num == 16:
                    cell.alignment = Alignment(horizontal="center")

                #**************  Agrega el total de Menores  ************************
        row_num += 2
        worksheet.merge_cells('A'+str(row_num+1)+':B'+str(row_num+1))
        cell = worksheet.cell(row=row_num+1, column=1)
        cell.value = "Total de Menores: " +' ' + str(total_menores)
        cell2 = worksheet.cell(row=row_num+2, column=1)
        cell2.value = "Total de Activos: " +' ' + str(total_activos)
        cell3 = worksheet.cell(row=row_num+3, column=1)
        cell3.value = "Total de Altas: " +' ' + str(total_altas)
        cell4 = worksheet.cell(row=row_num+4, column=1)
        cell4.value = "Total de Egresos: " +' ' + str(total_egresos)
        cell5 = worksheet.cell(row=row_num+5, column=1)
        cell5.value = "Total de Desincorporados: " +' ' + str(total_desincorporados)
        cell6 = worksheet.cell(row=row_num+6, column=1)
        cell6.value = "Total de Menores de 5 años: " +' ' + str(total_menores_5)
        cell7 = worksheet.cell(row=row_num+7, column=1)
        cell7.value = "Total de Menores de 2 años: " +' ' + str(total_menores_2)


    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Rep_listado_Menores.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    


class exportar_jornada(TemplateView):
    def get(self, request, *args, **kwargs):
        proyecto = request.GET.get('proyecto')
        jornada = request.GET.get('jornada')
        workbook = Workbook()
        bandera = True
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m')
        
        hojas = ["REGISTRO MENORES","ANTROPOMETRICO MENOR","REGISTRO DE EMBARAZADAS","REGISTRO DE LACTANTES","MEDICAMENTOS Y PRODUCTOS"]

        for hoja in hojas: 
            if bandera:
                worksheet = workbook.active
                worksheet.title = hoja
                bandera = False
                worksheet.merge_cells('A1:C1')
                first_cell = worksheet['A1']
                first_cell.value = "Fecha: " + fecha_fin
            else:
                worksheet = workbook.create_sheet(hoja)

    #*********  Crear encabezado en la hoja  *************
            worksheet.merge_cells('A2:D2')
            second_cell = worksheet['A2']
            second_cell.value = "Bokitas"
            second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")

            worksheet.merge_cells('A3:D3')
            third_cell = worksheet['A3']
            third_cell.value = "Bokitas Fundation    www.bokitas.org"
            third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  HOJA DE DATOS DE LOS MENORES  ********************************

    #*********  Registro de Datos de los Menores  *************
        worksheet = workbook.worksheets[0]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTROS DEL PERFIL DE MENORES"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        menores = Menor.objects.filter(proyecto=proyecto,jornada=jornada).order_by('-cedula_bef')

    #**************  Obtener el total de Menores  ***************
        total_menores = menores.count()
        total_activos = menores.values("estatus").filter(estatus="ACTIVO").count()
        total_altas = menores.values("estatus").filter(estatus="ALTA").count()
        total_egresos = menores.values("estatus").filter(estatus="EGRESO").count()
        total_desincorporados = menores.values("estatus").filter(estatus="DESINCORPORADO").count()
        total_menores_5 = menores.values("edad").filter(edad__lte=5).count()
        total_menores_2 = menores.values("edad").filter(edad__lte=2).count()

        titulos = ['PROYECTO','REPRESENTANTE','PARENTESCO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','DIAGNOSTICO PESO','DIAGNOSTICO TALLA','FECHA INGRESO','ESTATUS']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        for menor in menores:
            row_num += 1
            datos = [menor.proyecto,menor.cedula_bef,menor.parentesco,menor.cedula,menor.nombre,menor.apellido,menor.sexo,menor.fecha_nac.strftime('%d-%m-%Y'),menor.edad,menor.meses,menor.peso_actual,menor.talla_actual,menor.diagnostico_actual,menor.diagnostico_talla_actual,menor.fecha_ing_proyecto.strftime('%d-%m-%Y'),menor.estatus]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 3 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 15 or col_num == 16:
                    cell.alignment = Alignment(horizontal="center")

        #**************  Agrega el total de Menores  ************************
        row_num += 2
        worksheet.merge_cells('A'+str(row_num+1)+':B'+str(row_num+1))
        cell = worksheet.cell(row=row_num+1, column=1)
        cell.value = "Total de Menores: " +' ' + str(total_menores)
        cell2 = worksheet.cell(row=row_num+2, column=1)
        cell2.value = "Total de Activos: " +' ' + str(total_activos)
        cell3 = worksheet.cell(row=row_num+3, column=1)
        cell3.value = "Total de Altas: " +' ' + str(total_altas)
        cell4 = worksheet.cell(row=row_num+4, column=1)
        cell4.value = "Total de Egresos: " +' ' + str(total_egresos)
        cell5 = worksheet.cell(row=row_num+5, column=1)
        cell5.value = "Total de Desincorporados: " +' ' + str(total_desincorporados)
        cell6 = worksheet.cell(row=row_num+6, column=1)
        cell6.value = "Total de Menores de 5 años: " +' ' + str(total_menores_5)
        cell7 = worksheet.cell(row=row_num+7, column=1)
        cell7.value = "Total de Menores de 2 años: " +' ' + str(total_menores_2)

#*************  HOJA DE DATOS ANTROPOMETRICOS DEL MENORES  *********************

    #*********  Registro de Datos antropometricos Menores  *************
        worksheet = workbook.worksheets[1]
        worksheet.merge_cells('A4:W6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DATOS ANTROPOMETRICOS DEL MENOR"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_menores = AntropMenor.objects.filter(proyecto_id=proyecto,jornada=jornada).order_by('-cedula_bef','cedula_id').select_related('cedula')

        titulos = ['PROYECTO','REPRESENTANTE','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','FECHA JORNADA','EDAD','MESES','PESO','TALLA','CBI','PTR','PSE','CC','IMC','DIAGNOSTICO PESO','DIAGNOSTICO TALLA']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_menores:
            row_num += 1
            datos = [imc.proyecto,imc.cedula_bef,imc.cedula.cedula,imc.cedula.nombre,imc.cedula.apellido,imc.cedula.sexo,imc.cedula.fecha_nac.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.cedula.peso_actual,imc.cedula.talla_actual,imc.jornada,imc.edad,imc.meses,imc.peso,imc.talla,imc.cbi,imc.ptr,imc.pse,imc.cc,imc.imc,imc.diagnostico,imc.diagnostico_talla]

            if imc.cedula.cedula != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="center")
                    if col_num == 1 or col_num == 2 or col_num == 4 or col_num == 5 or col_num == 22 or col_num == 23:
                        cell.alignment = Alignment(horizontal="left")

                xCedula = imc.cedula.cedula
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 11:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")
                        if col_num == 22 or col_num == 23:
                            cell.alignment = Alignment(horizontal="left")



#*************  HOJA DE DATOS ANTROPOMETRICOS EMBARAZADAS  *********************

    #*********  Registro de Datos antropometricos Embarazadas  *************
        worksheet = workbook.worksheets[2]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DATOS ANTROPOMETRICOS EMBARAZADAS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_embarazos = AntropBef.objects.filter(proyecto=proyecto, jornada=jornada, embarazo_lactando = 'EMBARAZADA').order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA NAC.','FECHA JORNADA','EDAD','MESES','MESES EMBARAZO','PESO','TALLA','CBI','IMC','DIAGNOSTICO PESO','RIESGO','OBSERVACIONES']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_embarazos:
            row_num += 1
            datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac.strftime('%d-%m-%Y'),imc.jornada,imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]

            if imc.cedula_bef.cedula != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="center")
                    if col_num == 1 or col_num == 2 or col_num == 3 or col_num == 4:
                        cell.alignment = Alignment(horizontal="left")

                xCedula = imc.cedula_bef.cedula
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 7:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")


#*************  HOJA DE DATOS ANTROPOMETRICOS LACTANTES  *********************

    #*********  Registro de Datos antropometricos Lactante  *************
        worksheet = workbook.worksheets[3]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DATOS ANTROPOMETRICOS LACTANTES"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_embarazos = AntropBef.objects.filter(proyecto=proyecto,jornada=jornada, embarazo_lactando = 'LACTANDO').order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA NAC.','FECHA JORNADA','EDAD','MESES','MESES LACTANDO','PESO','TALLA','CBI','IMC','DIAGNOSTICO PESO','RIESGO','OBSERVACIONES']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas
        xCedula = 0

        for imc in imc_embarazos:
            row_num += 1
            datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac.strftime('%d-%m-%Y'),imc.jornada,imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]

            if imc.cedula_bef.cedula != xCedula:
                for col_num, cell_value in enumerate(datos, 1):
                    cell = worksheet.cell(row=row_num, column=col_num)
                    cell.value = str(cell_value)
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    cell.alignment = Alignment(horizontal="center")
                    if col_num == 1 or col_num == 2 or col_num == 3 or col_num == 4:
                        cell.alignment = Alignment(horizontal="left")

                xCedula = imc.cedula_bef.cedula
            else:
                for col_num, cell_value in enumerate(datos, 1):
                    if col_num > 7:
                        cell = worksheet.cell(row=row_num, column=col_num)
                        cell.value = str(cell_value)
                        cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                        cell.alignment = Alignment(horizontal="center")


#*************  HOJA DE DATOS ENTREGA MEDICAMENTOS PRODUCTOS  *********************

    #*********  Registro de Datos DATOS ENTREGA MEDICAMENTOS  *************
        worksheet = workbook.worksheets[4]
        worksheet.merge_cells('A4:H6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DE ENTREGA DE MEDICAMENTOS Y PRODUCTOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        medicamentos = Medicamento.objects.filter(proyecto=proyecto,jornada=jornada).order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA JORNADA','NOMBRE DEL PRODUCTO','DESCRIPCION DEL PRODUCTO','CANTIDAD']
        row_num = 7
        thin = Side(border_style="thin", color="000000")
        double = Side(border_style="double", color="000000")

    #********* asigna el titulo a las columnas  ************************
        for col_num, column_title in enumerate(titulos, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="E2D9F3")
            cell.border = Border(top=thin, left=thin, right=thin, bottom=double)
            cell.font  = Font(bold=True, size = 14, color="333399")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            adjusted_width = (len(cell.value) + 10) * 1.2
            worksheet.column_dimensions[get_column_letter(col_num)].width = adjusted_width

    #**************  Agrega la data a las celdas

        for med in medicamentos:
            row_num += 1
            datos = [med.cedula_bef.proyecto,med.cedula_bef.cedula,med.cedula_bef.nombre,med.cedula_bef.apellido,med.jornada,med.nombre,med.descripcion,med.cantidad]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                cell.alignment = Alignment(horizontal="center")
                if col_num == 1 or col_num == 2 or col_num == 3 or col_num == 4:
                    cell.alignment = Alignment(horizontal="left")


    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_por_Jornmada.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    


class estadistica_nutricional_proyecto(TemplateView):
    def get(self, request, *args, **kwargs):
        proyecto = request.GET.get('proyecto')
        workbook = Workbook()
        worksheet = workbook.create_sheet("ESTADISTICA NUTRICIONAL")
        wb = Workbook(write_only=True)
        ws = wb.create_sheet()

    #*********  Crear encabezado en la hoja  *************
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m')
        worksheet.merge_cells('A1:C1')
        first_cell = worksheet['A1']
        first_cell.value = "Fecha: " + fecha_fin
        
        worksheet.merge_cells('A2:E2')
        second_cell = worksheet['A2']
        second_cell.value = "Bokitas"
        second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")

        worksheet.merge_cells('A3:E3')
        third_cell = worksheet['A3']
        third_cell.value = "Bokitas Fundation    www.bokitas.org"
        third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  DATOS ESTADISTICA NUTRICIONAL  ********************************

    #*********  Registro de Datos  *************
        #worksheet = workbook.worksheets[0]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "RESPONSABLE DE HACER EL MERCADO, COCINAR Y FRECUENCIA DE COMPRA DE ALIMENTOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        nutricional = Nutricional.objects.filter(proyecto=proyecto)

    #********* asigna el titulo a los graficos  ************************

        worksheet = workbook.worksheets[1]
        worksheet.merge_cells('A7:G7')
        five_cell = worksheet['A7']
        five_cell.value = "RESPONSABLE DE HACER EL MERCADO Y COCINAR"
        five_cell.font  = Font(name = 'Tahoma', size = 12, bold = True, color="333399")
        five_cell.alignment = Alignment(horizontal="center", vertical="center")  

        worksheet = workbook.worksheets[1]
        worksheet.merge_cells('J7:O7')
        six_cell = worksheet['K7']
        six_cell.value = "FRECUENCIA DE LA COMPRA DE ALIMENTOS"
        six_cell.font  = Font(name = 'Tahoma', size = 12, bold = True, color="333399")
        six_cell.alignment = Alignment(horizontal="center", vertical="center") 



    #**************  Obtener el total de las encuestas  ***************
        total_encuestados = nutricional.count()

        padre_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza__icontains="Padre").count()
        madre_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza__icontains="Madre").count()
        abuelo_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza__icontains="Abuelo(a)").count()
        tio_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza__icontains="Tio(a)").count()
        otros_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza__icontains="Otros").count()

        padre_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza__icontains="Padre").count()
        madre_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza__icontains="Madre").count()
        abuelo_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza__icontains="Abuelo(a)").count()
        tio_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza__icontains="Tio(a)").count()
        otros_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza__icontains="Otros").count()
        
        fecuencia_diario = nutricional.values("frecuencia").filter(frecuencia__icontains="diario").count()
        fecuencia_2_3 = nutricional.values("frecuencia").filter(frecuencia__icontains="2-3 días").count()
        fecuencia_semanal = nutricional.values("frecuencia").filter(frecuencia__icontains="Semanal").count()
        fecuencia_quincenal = nutricional.values("frecuencia").filter(frecuencia__icontains="Quincenal").count()


    #**************  Agrega la data a las celdas

        row_num = 7
        rows = [
                ('Integrantes', 'Hace Mercado', 'Quien Cocina'),
                ('Madre', madre_mercado, madre_cocina),
                ('Padre', padre_mercado, padre_cocina),
                ('Abuela', abuelo_mercado, abuelo_cocina),
                ('Tios', tio_mercado, tio_cocina),
                ('Otros', otros_mercado, otros_cocina),
            ]
        for row in rows:
            ws.append(row)
        chart1 = BarChart()
        chart1.type = "col"
        chart1.style = 10
        chart1.title = "Bar Chart"
        chart1.y_axis.title = 'Número de Casos'
        chart1.x_axis.title = 'Integrantes'

        data = Reference(ws, min_col=2, min_row=1, max_row=7, max_col=3)
        cats = Reference(ws, min_col=1, min_row=2, max_row=7)
        chart1.add_data(data, titles_from_data=True)
        chart1.set_categories(cats)
        chart1.shape = 4
        ws.add_chart(chart1, "A12")


    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_Estadistica_Nutricional.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    


class estadistica_nutricional_jornada(TemplateView):
    def get(self, request,  pk, *args, **kwargs):
        jornada = request.GET.get('jornada')
        beneficiarios = Beneficiario.objects.filter(id=pk)
        proyecto = beneficiarios[0].proyecto
        workbook = Workbook()
        worksheet = workbook.create_sheet("ESTADISTICA NUTRICIONAL")
        wb = Workbook(write_only=True)
        ws = wb.create_sheet()

    #*********  Crear encabezado en la hoja  *************
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m')
        worksheet.merge_cells('A1:C1')
        first_cell = worksheet['A1']
        first_cell.value = "Fecha: " + fecha_fin
        
        worksheet.merge_cells('A2:D2')
        second_cell = worksheet['A2']
        second_cell.value = "Bokitas"
        second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")

        worksheet.merge_cells('A3:D3')
        third_cell = worksheet['A3']
        third_cell.value = "Bokitas Fundation    www.bokitas.org"
        third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  DATOS ESTADISTICA NUTRICIONAL  ********************************

    #*********  Registro de Datos  *************
        worksheet = workbook.worksheets[0]
        worksheet.merge_cells('A4:P6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "RESPONSABLE DE HACER EL MERCADO, COCINAR Y FRECUENCIA DE COMPRA DE ALIMENTOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        nutricional = Nutricional.objects.filter(proyecto=proyecto,jornada=jornada).order_by('-cedula_bef')

    #**************  Obtener el total de las encuestas  ***************
        total_encuestados = nutricional.count()

        padre_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza="Padre").count()
        madre_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza="Madre").count()
        abuelo_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza="Abuelo(a)").count()
        tio_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza="Tio(a)").count()
        otros_mercado = nutricional.values("mercado_lorealiza").filter(mercado_lorealiza="Otros").count()

        padre_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza="Padre").count()
        madre_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza="Madre").count()
        abuelo_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza="Abuelo(a)").count()
        tio_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza="Tio(a)").count()
        otros_cocina = nutricional.values("cocina_lorealiza").filter(cocina_lorealiza="Otros").count()
        
        fecuencia_diario = nutricional.values("frecuencia").filter(frecuencia="diario").count()
        fecuencia_2_3 = nutricional.values("frecuencia").filter(frecuencia="2-3 días").count()
        fecuencia_semanal = nutricional.values("frecuencia").filter(frecuencia="Semanal").count()
        fecuencia_quincenal = nutricional.values("frecuencia").filter(frecuencia="Quincenal").count()

    #********* asigna el titulo a los graficos  ************************
        worksheet = workbook.worksheets[0]
        worksheet.merge_cells('A5:E5')
        fourth_cell = worksheet['A5']
        fourth_cell.value = "RESPONSABLE DE HACER EL MERCADO Y COCINAR"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")  

        worksheet = workbook.worksheets[0]
        worksheet.merge_cells('H5:L5')
        fourth_cell = worksheet['A5']
        fourth_cell.value = "FRECUENCIA DE LA COMPRA DE ALIMENTOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center") 



    #**************  Agrega la data a las celdas

        row_num = 7
        rows = [
                ('Integrantes', 'Hace Mercado', 'Quien Cocina'),
                ('Madre', madre_mercado, madre_cocina),
                ('Padre', padre_mercado, padre_cocina),
                ('Abuela', abuelo_mercado, abuelo_cocina),
                ('Tios', tio_mercado, tio_cocina),
                ('Otros', otros_mercado, otros_cocina),
            ]

        chart1 = BarChart()
        chart1.type = "col"
        chart1.style = 10
        chart1.title = "Bar Chart"
        chart1.y_axis.title = 'Número de Casos'
        chart1.x_axis.title = 'Integrantes'

        data = Reference(ws, min_col=2, min_row=1, max_row=7, max_col=3)
        cats = Reference(ws, min_col=1, min_row=2, max_row=7)
        chart1.add_data(data, titles_from_data=True)
        chart1.set_categories(cats)
        chart1.shape = 4
        ws.add_chart(chart1, "A10")


    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_Estadistica_Nutricional.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    
