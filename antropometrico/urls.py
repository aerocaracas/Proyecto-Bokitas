from django.urls import path
from . import views

urlpatterns = [
    path('antropometrico/', views.antropometrico, name='antropometrico'),

]