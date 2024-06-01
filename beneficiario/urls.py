from django.urls import path
from beneficiario import views

urlpatterns = [
    path('beneficiario/', views.beneficiario, name='beneficiario'),
    path('beneficiario/crear/', views.beneficiario_crear, name='beneficiario_crear'),
    path('beneficiario/<int:pk>/', views.beneficiario_detalle, name='beneficiario_detalle'),
    path('beneficiario/<int:pk>/actualizar/', views.beneficiario_actualizar, name='beneficiario_actualizar'),
    path('beneficiario/<int:pk>/eliminar/', views.beneficiario_eliminar, name='beneficiario_eliminar'),
    path('beneficiario/<int:pk>/menor/crear/', views.menor_crear, name='menor_crear'),
    path('beneficiario/<int:pk>/menor/detalle/', views.menor_detalle, name='menor_detalle'),
    path('beneficiario/<int:pk>/familiar/crear/', views.familiar_crear, name='familiar_crear'),
    path('beneficiario/<int:pk>/antrop_benef/crear/', views.antrop_benef_crear, name='antrop_benef_crear'),
    path('beneficiario/<int:pk>/antrop_benef/calcular/', views.antrop_benef_calcular, name='antrop_benef_calcular'),
    path('beneficiario/<int:pk>/medicamento/crear/', views.medicamento_crear, name='medicamento_crear'),
    path('beneficiario/<int:pk>/medica/crear/', views.medica_crear, name='medica_crear'),
    path('beneficiario/<int:pk>/medica/detalle/', views.medica_detalle, name='medica_detalle'),
    path('beneficiario/<int:pk>/medica/eliminar', views.medica_eliminar, name='medica_eliminar'),
    

]