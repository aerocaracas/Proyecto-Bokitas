from django.urls import path
from . import views

urlpatterns = [
    path('socioeconomico/', views.socioeconomico, name='socioeconomico'),

]