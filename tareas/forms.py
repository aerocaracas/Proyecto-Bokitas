from django.forms import ModelForm
from bokitas.models import Tareas

class TareaForm(ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion','importante']

