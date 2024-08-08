from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor, Familia, AntropBef, AntropMenor, Medicamento, Medica, Nutricional
from django.db.models import Q
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill,Side

# Create your views here.

class exportar_proyecto(TemplateView):

    def get(self, request, *args, **kwargs):
        query = Beneficiario.objects.all()
        wb = Workbook()
        bandera = True
        hojas = 5
        cont = 1
        for hoja in query:
            if bandera:
                ws = wb.active
                bandera = False
            else:
                ws = wb.create_sheet('hoja'+str(cont))
            cont += 1
        
    #*********  Establecer el nombre del Archivo *******
        nombre_archvo = "Reporte_por_Proyecto.xlsx"
    
    #*********  Definir el tipo de respuesta que se va a dar ***********
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archvo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response
    
