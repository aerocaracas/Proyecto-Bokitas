from django.urls import path
from tareas import views

urlpatterns = [
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/completada', views.tarea_completada, name='tarea_completada'),
    path('tareas/crear/', views.tarea_crear, name='tarea_crear'),
    path('tareas/<int:tarea_id>/', views.tarea_detalle, name='tarea_detalle'),
    path('tareas/<int:tarea_id>/completar', views.tarea_complatar, name='tarea_completar'),
    path('tareas/<int:tarea_id>/eliminar', views.tarea_eliminar, name='tarea_eliminar'),

]