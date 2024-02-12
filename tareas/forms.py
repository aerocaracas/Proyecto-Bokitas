from django.forms import ModelForm
from bokitas.models import Tarea

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion','importante']

