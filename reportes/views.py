from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica, Nutricional
from django.db.models import Q
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from datetime import datetime, date
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

# Create your views here.

class exportar_proyecto(TemplateView):

    def get(self, request, *args, **kwargs):
    #####    query = Beneficiario.objects.all()
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
            third_cell.value = "Bokitas Fundation  www.bokitas.org"
            third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")
        
#***********************  HOJA DE DATOS DE LOS BENEFICIARIOS  ********************************

    #*********  Registro de Datos de los Beneficiario  *************
        worksheet = workbook.worksheets[0]
       # worksheet = workbook['REGISTRO BENEFICIARIOS']
        worksheet.merge_cells('A4:U6')
        fourth_cell = worksheet['A4']
        fourth_cell.value = "REGISTRO DE LOS BENEFICIARIOS"
        fourth_cell.font  = Font(name = 'Tahoma', size = 16, bold = True, color="333399")
        fourth_cell.alignment = Alignment(horizontal="center", vertical="center")      

        beneficiarios = Beneficiario.objects.all()
        titulos = ['PROYECTO','CÉDULA','NOMBRE','APELLIDO','SEXO','FECHA NAC.','EDAD','MESES','EMBARAZADA','LACTANDO','ESTADO CIVIL','EDUCACIÓN','PROFESIÓN','LABORAL','TELEFONO','CORREO','DIRECCIÓN','CIUDAD','ESTADO','ESTATUS','NÚMERO DE CUENTA']
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
            datos = [beneficiario.proyecto,beneficiario.cedula,beneficiario.nombre,beneficiario.apellido,beneficiario.sexo,beneficiario.fecha_nac,beneficiario.edad,beneficiario.meses,beneficiario.embarazada,beneficiario.lactante,beneficiario.estado_civil,beneficiario.educacion,beneficiario.profesion,beneficiario.laboral,beneficiario.telefono,beneficiario.correo,beneficiario.direccion,beneficiario.ciudad,beneficiario.estado,beneficiario.estatus,beneficiario.numero_cuenta]

            for col_num, cell_value in enumerate(datos, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = str(cell_value)
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                if col_num == 6 or col_num == 7 or col_num == 8 or col_num == 9 or col_num == 10 or col_num == 20:
                    cell.alignment = Alignment(horizontal="center")

                




    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_por_Proyecto.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    
