from django.urls import path
from reportes import views
from reportes.views import exportar_proyecto, exportar_beneficiario_detalle

urlpatterns = [
    path('exportar_proyecto/', exportar_proyecto.as_view(), name = 'exportar_proyecto'),
    path('exportar_proyecto/<int:pk>/', exportar_beneficiario_detalle.as_view(), name = 'exportar_beneficiario_detalle'),

]