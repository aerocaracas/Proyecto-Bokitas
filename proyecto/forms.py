from django.forms import ModelForm
from bokitas.models import Proyecto

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['cedula', 'nombre','apellido']

