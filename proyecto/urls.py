from django.urls import path
from proyecto import views

urlpatterns = [
    path('proyecto/', views.proyecto, name='proyecto'),
    path('proyecto/<int:tarea_id>/', views.proyecto_detalle, name='proyecto_detalle'),
]
