from django.urls import path
from beneficiario import views


urlpatterns = [
    path('beneficiario/', views.beneficiario, name='beneficiario'),
    path('beneficiario/crear/', views.beneficiario_crear, name='beneficiario_crear'),
    path('beneficiario/<int:pk>/', views.beneficiario_detalle, name='beneficiario_detalle'),
    path('beneficiario/<int:pk>/actualizar/', views.beneficiario_actualizar, name='beneficiario_actualizar'),
    path('beneficiario/<int:pk>/eliminar/', views.beneficiario_eliminar, name='beneficiario_eliminar'),
 
    path('beneficiario/<int:pk>/familiar/crear/', views.familiar_crear, name='familiar_crear'),
    path('beneficiario/<int:pk>/familiar/<int:id>/actualizar', views.familiar_actualizar, name='familiar_actualizar'),
    path('beneficiario/<int:pk>/familiar/<int:id>/eliminar', views.familiar_eliminar, name='familiar_eliminar'),

    path('beneficiario/<int:pk>/imc_benef/', views.imc_benef, name='imc_benef'),
    path('beneficiario/<int:pk>/imc_benef/<int:idimc>/imc_benef_riesgo', views.imc_benef_riesgo, name='imc_benef_riesgo'),
    path('beneficiario/<int:pk>/imc_benef/<int:id>/imc_benef_detalle', views.imc_benef_detalle, name='imc_benef_detalle'),
    path('beneficiario/<int:pk>/imc_benef/<int:id>/eliminar', views.imc_benef_eliminar, name='imc_benef_eliminar'),
    
    path('beneficiario/<int:pk>/medicamento/crear/', views.medicamento_crear, name='medicamento_crear'),
    path('beneficiario/<int:pk>/medicamento/<int:id>/eliminar', views.medicamento_eliminar, name='medicamento_eliminar'),
    
    path('beneficiario/<int:pk>/nutricioinal/<int:id>/nutricional_beneficiario', views.nutricional_beneficiario, name='nutricional_beneficiario'),

    path('beneficiario/crear/load_jornadas_benef/', views.load_jornadas_benef, name='load_jornadas_benef'),
    path('beneficiario/<int:pk>/actualizar/load_jornadas_benef_act/', views.load_jornadas_benef_act, name='load_jornadas_benef_act'),
    
]