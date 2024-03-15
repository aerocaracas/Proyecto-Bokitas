from django.urls import path
from beneficiario import views

urlpatterns = [
    path('beneficiario/', views.beneficiario, name='beneficiario'),
    path('beneficiario/crear/', views.beneficiario_crear, name='beneficiario_crear'),
    path('beneficiario/<int:pk>/', views.beneficiario_detalle, name='beneficiario_detalle'),
    path('beneficiario/<int:pk>/actualizar/', views.beneficiario_actualizar, name='beneficiario_actualizar'),
    path('beneficiario/<int:pk>/eliminar', views.beneficiario_eliminar, name='beneficiario_eliminar'),
    path('menor/crear/', views.menor_crear, name='menor_crear'),
    path('familiar/crear/', views.familiar_crear, name='familiar_crear'),
    path('antropBenef/crear/', views.antrop_benef_crear, name='antrop_benef_crear'),

]