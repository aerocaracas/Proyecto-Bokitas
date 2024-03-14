from django.forms import ModelForm
from bokitas.models import Proyecto

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['proyecto','estatus','nombre_centro', 'direccion','estado','ciudad','representante','telefono','correo']

        labels = {'proyecto':'Proyecto','estatus':'Estatus','nombre_centro':'Nombre del Centro', 'direccion':'Dirección','estado':'Estado','ciudad':'Ciudad','representante':'Representante','telefono':'Teléfono','correo':'Correo'}
