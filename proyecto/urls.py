from django.urls import path
from proyecto import views

urlpatterns = [
    path('proyecto/', views.proyecto, name='proyecto'),
    path('proyecto/crear/', views.proyecto_crear, name='proyecto_crear'),
    path('proyecto/<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),
]
