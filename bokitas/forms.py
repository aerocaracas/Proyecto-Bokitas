from django.forms import ModelForm
from .models import Tareas

class tareaCrearForm(ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion','importante']

