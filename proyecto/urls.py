from django.urls import path
from proyecto import views

urlpatterns = [
    path('proyecto/', views.proyecto, name='proyecto'),
    path('proyecto/crear/', views.proyecto_crear, name='proyecto_crear'),
    path('proyecto/<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('proyecto/<int:pk>/actualizar/', views.proyecto_actualizar, name='proyecto_actualizar'),
    path('proyecto/<int:pk>/jornada/', views.proyecto_jornada, name='proyecto_jornada'),
    path('proyecto/<int:pk>/eliminar', views.proyecto_eliminar, name='proyecto_eliminar'),
    path('jornada/<int:pk>/eliminar/<int:id>/', views.jornada_eliminar, name='jornada_eliminar'),
    path('cities', views.cities, name = "cities")
]
