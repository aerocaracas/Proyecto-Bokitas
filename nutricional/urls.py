from django.urls import path
from nutricional import views

urlpatterns = [
    path('nutricional/', views.nutricional, name='nutricional'),
    path('nutricional/crear/', views.nutricional_crear, name='nutricional_crear'),
    path('nutricional/<int:pk>/actualizar/', views.nutricional_actualizar, name='nutricional_actualizar'),
    path('nutricional/<int:pk>/eliminar/', views.nutricional_eliminar, name='nutricional_eliminar'),
    path('nutricional/crear/load_jornadas_nutri/', views.load_jornadas_nutri, name='load_jornadas_nutri'),

]