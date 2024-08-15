from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica, Nutricional
from django.db.models import Q
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

# Create your views here.

class exportar_proyecto(TemplateView):
    def get(self, request, *args, **kwargs):
    
        workbook = Workbook()
        bandera = True
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m')
        
        hojas = ["REGISTRO BENEFICIARIOS","REGISTRO MENORES","ANTROPOMETRICOS MENORES","ANTROPOMETRICO EMBARAZADAS","ANTROPOMETRICO LACTANTE"]

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
       # worksheet = workbook['REGISTRO BENEFICIARIOS']
        worksheet.merge_cells('A4:W6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DE LOS BENEFICIARIOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        beneficiarios = Beneficiario.objects.all().order_by('cedula')
        
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
            datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac.strftime('%d-%m-%Y'),beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 6 or col_num == 7 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 22:
                    cell.alignment = Alignment(horizontal="center")


#***********************  HOJA DE DATOS DE LOS MENORES  ********************************

    #*********  Registro de Datos de los Menores  *************
        worksheet = workbook.worksheets[1]
        worksheet.merge_cells('A4:O6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTROS DEL PERFIL DE MENORES"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        menores = Menor.objects.all().order_by('-cedula_bef')

        titulos = ['PROYECTO','REPRESENTANTE','PARENTESCO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','DIAGNOSTICO PESO','DIAGNOSTICO TALLA','FECHA INGRESO']
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
            datos = [menor.proyecto,menor.cedula_bef,menor.parentesco,menor.cedula,menor.nombre,menor.apellido,menor.sexo,menor.fecha_nac.strftime('%d-%m-%Y'),menor.edad,menor.meses,menor.peso_actual,menor.talla_actual,menor.diagnostico_actual,menor.diagnostico_talla_actual,menor.fecha_ing_proyecto.strftime('%d-%m-%Y')]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 3 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 15:
                    cell.alignment = Alignment(horizontal="center")


#*************  HOJA DE DATOS ANTROPOMETRICOS DEL  MENORES  *********************

    #*********  Registro de Datos antropometricos Menores  *************
        worksheet = workbook.worksheets[2]
        worksheet.merge_cells('A4:W6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DATOS ANTROPOMETRICOS DEL MENOR"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        imc_menores = AntropMenor.objects.all().order_by('-cedula_bef','cedula_id').select_related('cedula')

        titulos = ['PROYECTO','REPRESENTANTE','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','PESO ACTUAL','TALLA ACTUAL','FECHA EVALUACIÓN','EDAD','MESES','PESO','TALLA','CBI','PTR','PSE','CC','IMC','DIAGNOSTICO PESO','DIAGNOSTICO TALLA']
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
            datos = [imc.proyecto,imc.cedula_bef,imc.cedula.cedula,imc.cedula.nombre,imc.cedula.apellido,imc.cedula.sexo,imc.cedula.fecha_nac.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.cedula.peso_actual,imc.cedula.talla_actual,imc.fecha.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.peso,imc.talla,imc.cbi,imc.ptr,imc.pse,imc.cc,imc.imc,imc.diagnostico,imc.diagnostico_talla]

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

        imc_embarazos = AntropBef.objects.filter(embarazo_lactando = 'EMBARAZADA').order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA NAC.','FECHA EVALUACIÓN','EDAD','MESES','MESES EMBARAZO','PESO','TALLA','CBI','IMC','DIAGNOSTICO PESO','RIESGO','OBSERVACIONES']
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
            datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac.strftime('%d-%m-%Y'),imc.fecha.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]

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

        imc_embarazos = AntropBef.objects.filter(embarazo_lactando = 'LACTANDO').order_by('-cedula_bef').select_related('cedula_bef')

        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','FECHA NAC.','FECHA EVALUACIÓN','EDAD','MESES','MESES LACTANDO','PESO','TALLA','CBI','IMC','DIAGNOSTICO PESO','RIESGO','OBSERVACIONES']
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
            datos = [imc.cedula_bef.proyecto,imc.cedula_bef.cedula,imc.cedula_bef.nombre,imc.cedula_bef.apellido,imc.cedula_bef.fecha_nac.strftime('%d-%m-%Y'),imc.fecha.strftime('%d-%m-%Y'),imc.edad,imc.meses,imc.tiempo_gestacion,imc.peso,imc.talla,imc.cbi,imc.imc,imc.diagnostico,imc.riesgo,imc.observacion]

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

    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_por_Proyecto.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    


class exportar_beneficiario_detalle(TemplateView):
    def get(self, request,  pk, *args, **kwargs):
        workbook = Workbook()
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m') 
        worksheet = workbook.active
        worksheet.title = "REGISTRO BENEFICIARIOS"
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
        fourth_cell.value = "REGISTRO DE LOS BENEFICIARIOS"
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
            datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac.strftime('%d-%m-%Y'),beneficiario.edad,beneficiario.meses,beneficiario.nacionalidad,beneficiario.num_hijos,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 6 or col_num == 7 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 11 or col_num == 12 or col_num == 22:
                    cell.alignment = Alignment(horizontal="center")

    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_Beneficiario_detalle.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    
