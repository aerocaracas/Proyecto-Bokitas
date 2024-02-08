from django.urls import path
from . import views

urlpatterns = [
    path('proyecto/', views.proyecto, name='proyecto'),

]
