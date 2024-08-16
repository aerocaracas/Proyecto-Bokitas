from django.urls import path
from reportes import views
from reportes.views import exportar_proyecto, exp_beneficiario_detalle, listado_beneficiario

urlpatterns = [
    path('exportar_proyecto/', exportar_proyecto.as_view(), name = 'exportar_proyecto'),
    path('exp_beneficiario_detalle/<int:pk>/', exp_beneficiario_detalle.as_view(), name = 'exp_beneficiario_detalle'),
    path('listado_beneficiario/', listado_beneficiario.as_view(), name = 'listado_beneficiario'),

]