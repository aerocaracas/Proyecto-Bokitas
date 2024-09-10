from django.urls import path
from menores import views

urlpatterns = [
    path('menores/', views.menores, name='menores'),
    path('beneficiario/<int:pk>/menor/crear/', views.menor_crear, name='menor_crear'),
    path('beneficiario/<int:pk>/menor/<int:id>/detalle/', views.menor_detalle, name='menor_detalle'),
    path('beneficiario/<int:pk>/menor/<int:id>/actualizar', views.menor_actualizar, name='menor_actualizar'),
    path('beneficiario/<int:pk>/menor/<int:id>/eliminar', views.menor_eliminar, name='menor_eliminar'),

    path('beneficiario/<int:pk>/menor/<int:id>/medica/crear/', views.medica_crear, name='medica_crear'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/<int:idmed>/detalle/', views.medica_detalle, name='medica_detalle'),
    path('beneficiario/<int:pk>/menor/<int:id>/medica/<int:idmed>/medica_eliminar/', views.medica_eliminar, name='medica_eliminar'),

    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/', views.imc_menor_crear, name='imc_menor_crear'),
    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/<int:idimc>/imc_menor_riesgo', views.imc_menor_riesgo, name='imc_menor_riesgo'),
    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/<int:idimc>/imc_menor_detalle', views.imc_menor_detalle, name='imc_menor_detalle'),
    path('beneficiario/<int:pk>/menor/<int:id>/imc_menor/<int:idimc>/eliminar', views.imc_menor_eliminar, name='imc_menor_eliminar'),
    
    path('beneficiario/<int:pk>/menor/crear/load_jornadas_menor/', views.load_jornadas_menor, name='load_jornadas_menor'),

]