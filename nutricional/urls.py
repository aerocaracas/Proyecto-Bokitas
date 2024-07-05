from django.urls import path
from . import views

urlpatterns = [
    path('nutricional/', views.nutricional, name='nutricional'),
    path('nutricional/crear/', views.nutricional_crear, name='nutricional_crear'),

]