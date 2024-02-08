from django.urls import path
from . import views

urlpatterns = [
    path('nutricional/', views.nutricional, name='nutricional'),

]