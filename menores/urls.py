from django.urls import path
from menores import views

urlpatterns = [
    path('menores/', views.menores, name='menores'),

]