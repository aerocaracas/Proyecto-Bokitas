from django.urls import path
from . import views

urlpatterns = [
    path('medica/', views.medica, name='medica'),

]