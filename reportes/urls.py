from django.urls import path
from reportes import views
from reportes.views import exportar_proyecto, exportar_jornada, exp_beneficiario_detalle, listado_beneficiario, listado_menores,estadistica_nutricional_proyecto

urlpatterns = [
    path('exportar_proyecto/', exportar_proyecto.as_view(), name = 'exportar_proyecto'),
    path('exp_beneficiario_detalle/<int:pk>/', exp_beneficiario_detalle.as_view(), name = 'exp_beneficiario_detalle'),
    path('proyecto/exportar_jornada/', exportar_jornada.as_view(), name = 'exportar_jornada'),
    path('listado_beneficiario/', listado_beneficiario.as_view(), name = 'listado_beneficiario'),
    path('listado_menores/', listado_menores.as_view(), name = 'listado_menores'),
    path('estadistica_nutricional_proyecto/', estadistica_nutricional_proyecto.as_view(), name = 'estadistica_nutricional_proyecto'),

]