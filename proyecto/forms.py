from django.forms import ModelForm
from bokitas.models import Proyecto

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['proyecto','estatus','nombre_centro', 'direccion','estado','ciudad','representante','telefono','correo']

