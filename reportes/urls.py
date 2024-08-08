from django.urls import path
from reportes import views
from reportes.views import exportar_proyecto

urlpatterns = [
    path('exportar_proyecto/', exportar_proyecto.as_view(), name = 'exportar_proyecto'),

]