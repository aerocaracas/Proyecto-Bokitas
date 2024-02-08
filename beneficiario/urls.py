from django.urls import path
from . import views

urlpatterns = [
    path('beneficiario/', views.beneficiario, name='beneficiario'),

]