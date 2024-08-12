from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica, Nutricional
from django.db.models import Q
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from datetime import datetime, date
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill,Side

# Create your views here.

class exportar_proyecto(TemplateView):

    def get(self, request, *args, **kwargs):
    #####    query = Beneficiario.objects.all()
        workbook = Workbook()
        bandera = True
        fecha = datetime.now()
        fecha_fin = fecha.strftime('%d-%m-%Y - hora: %H:%m')
        
        titulo = ["REGISTRO BENEFICIARIOS","REGISTRO MENORES","ANTROPOMETRICOS MENORES","ANTROPOMETRICO EMBARAZADAS","ANTROPOMETRICO LACTANTE"]

        for titu in titulo: 
            if bandera:
                worksheet = workbook.active
                worksheet.title = titu
                bandera = False
                worksheet.merge_cells('A1:C1')
                first_cell = worksheet['A1']
                first_cell.value = "Fecha: " + fecha_fin
            else:
                worksheet = workbook.create_sheet(titu)

    #*********  Crear encabezado en la hoja  *************
            worksheet.merge_cells('A2:C2')
            second_cell = worksheet['A2']
            second_cell.value = "Bokitas"
            second_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 52, bold = True, color="6F42C1")
            worksheet.merge_cells('A3:C3')
            third_cell = worksheet['A3']
            third_cell.value = "Bokitas Fundation  www.bokitas.org"
            third_cell.font  = Font(name = 'Tw Cen MT Condensed Extra Bold', size = 12, bold = True, color="6F42C1")





    #*********  Define los titulos de las columnas  ***************
        columns = ['Country Name','Country Code','Year', 'Value in USD']
        row_num = 3

        # Assign the titles for each cell of the header
        for col_num, column_title in enumerate(columns, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.fill = PatternFill("solid", fgColor="50C878")
            cell.font  = Font(bold=True, color="F7F6FA")
            third_cell = worksheet['D3']
            third_cell.alignment = Alignment(horizontal="right")





        
    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_por_Proyecto.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        workbook.save(response)
        return response
    
