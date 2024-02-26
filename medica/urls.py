from django.urls import path
from medica import views

urlpatterns = [
    path('medica/', views.medica, name='medica'),
    path('medica/crear/', views.medica_crear, name='medica_crear'),
    path('medica/<int:pk>/', views.medica_detalle, name='medica_detalle'),
    path('medica/<int:pk>/eliminar', views.medica_eliminar, name='medica_eliminar'),
    
    ]