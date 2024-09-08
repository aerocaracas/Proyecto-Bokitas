from django.urls import path
from beneficiario import views


urlpatterns = [
    path('beneficiario/', views.beneficiario, name='beneficiario'),
    path('beneficiario/crear/', views.beneficiario_crear, name='beneficiario_crear'),
    path('beneficiario/<int:pk>/', views.beneficiario_detalle, name='beneficiario_detalle'),
    path('beneficiario/<int:pk>/actualizar/', views.beneficiario_actualizar, name='beneficiario_actualizar'),
    path('beneficiario/<int:pk>/eliminar/', views.beneficiario_eliminar, name='beneficiario_eliminar'),
    path('beneficiario/<int:pk>/menor/crear/', views.menor_crear, name='menor_crear'),
    path('beneficiario/<int:pk>/menor/<int:id>/detalle/', views.menor_detalle, name='menor_detalle'),
    path('beneficiario/<int:pk>/menor/<int:id>/actualizar', views.menor_actualizar, name='menor_actualizar'),
    path('beneficiario/<int:pk>/menor/<int:id>/eliminar', views.menor_eliminar, name='menor_eliminar'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/crear/', views.medica_crear, name='medica_crear'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/<int:idmed>/detalle/', views.medica_detalle, name='medica_detalle'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/<int:idmed>/medica_eliminar/', views.medica_eliminar, name='medica_eliminar'),
    path('beneficiario/<int:pk>/familiar/crear/', views.familiar_crear, name='familiar_crear'),
    path('beneficiario/<int:pk>/familiar/<int:id>/actualizar', views.familiar_actualizar, name='familiar_actualizar'),
    path('beneficiario/<int:pk>/familiar/<int:id>/eliminar', views.familiar_eliminar, name='familiar_eliminar'),
    path('beneficiario/<int:pk>/imc_benef/', views.imc_benef, name='imc_benef'),
    path('beneficiario/<int:pk>/imc_benef/<int:idimc>/imc_benef_riesgo', views.imc_benef_riesgo, name='imc_benef_riesgo'),
    path('beneficiario/<int:pk>/imc_benef/<int:id>/imc_benef_detalle', views.imc_benef_detalle, name='imc_benef_detalle'),
    path('beneficiario/<int:pk>/imc_benef/<int:id>/eliminar', views.imc_benef_eliminar, name='imc_benef_eliminar'),
    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/', views.imc_menor_crear, name='imc_menor_crear'),
    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/<int:idimc>/imc_menor_riesgo', views.imc_menor_riesgo, name='imc_menor_riesgo'),
    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/<int:idimc>/imc_menor_detalle', views.imc_menor_detalle, name='imc_menor_detalle'),
    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/<int:idimc>/eliminar', views.imc_menor_eliminar, name='imc_menor_eliminar'),
    path('beneficiario/<int:pk>/medicamento/crear/', views.medicamento_crear, name='medicamento_crear'),
    path('beneficiario/<int:pk>/medicamento/<int:id>/eliminar', views.medicamento_eliminar, name='medicamento_eliminar'),
    path('beneficiario/<int:pk>/nutricioinal/<int:id>/nutricional_beneficiario', views.nutricional_beneficiario, name='nutricional_beneficiario'),
    path('beneficiario/crear/load_jornadas_benef/', views.load_jornadas_benef, name='load_jornadas_benef'),
    path('beneficiario/<int:pk>/actualizar/load_jornadas_benef_act/', views.load_jornadas_benef_act, name='load_jornadas_benef_act'),
    path('beneficiario/<int:pk>/menor/crear/load_jornadas_menor/', views.load_jornadas_menor, name='load_jornadas_menor'),


]