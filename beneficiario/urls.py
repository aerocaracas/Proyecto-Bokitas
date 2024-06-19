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
    path('beneficiario/<int:pk>/menor/<int:id>/menor_actualizar', views.menor_actualizar, name='menor_actualizar'),
    path('beneficiario/<int:pk>/menor/<int:id>/menor_eliminar', views.menor_eliminar, name='menor_eliminar'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/crear/', views.medica_crear, name='medica_crear'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/detalle/', views.medica_detalle, name='medica_detalle'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/eliminar', views.medica_eliminar, name='medica_eliminar'),
    path('beneficiario/<int:pk>/familiar/crear/', views.familiar_crear, name='familiar_crear'),
    path('beneficiario/<int:pk>/familiar/<int:id>/familiar_actualizar', views.familiar_actualizar, name='familiar_actualizar'),
    path('beneficiario/<int:pk>/familiar/<int:id>/familiar_eliminar', views.familiar_eliminar, name='familiar_eliminar'),
    path('beneficiario/<int:pk>/imc_benef/', views.imc_benef, name='imc_benef'),
    path('beneficiario/<int:pk>/imc_benef/<int:idimc>/imc_benef_riesgo', views.imc_benef_riesgo, name='imc_benef_riesgo'),
    path('beneficiario/<int:pk>/imc_benef/<int:id>/imc_benef_detalle', views.imc_benef_detalle, name='imc_benef_detalle'),
    path('beneficiario/<int:pk>/imc_benef/<int:id>/imc_benef_eliminar', views.imc_benef_eliminar, name='imc_benef_eliminar'),
    path('beneficiario/<int:pk>/medicamento/crear/', views.medicamento_crear, name='medicamento_crear'),
    path('beneficiario/<int:pk>/medicamento/<int:id>/medicamento_eliminar', views.medicamento_eliminar, name='medicamento_eliminar'),

    

]