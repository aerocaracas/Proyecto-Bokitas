from django.urls import path
from beneficiario import views

urlpatterns = [
    path('beneficiario/', views.beneficiario, name='beneficiario'),
    path('beneficiario/crear/', views.beneficiario_crear, name='beneficiario_crear'),
    path('beneficiario/<int:pk>/', views.beneficiario_detalle, name='beneficiario_detalle'),
    path('beneficiario/<int:pk>/eliminar', views.beneficiario_eliminar, name='beneficiario_eliminar'),

]