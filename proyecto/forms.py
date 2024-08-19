from django.forms import ModelForm
from bokitas.models import Proyecto,Jornada
from django.forms.widgets import NumberInput 

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['proyecto','estatus','nombre_centro', 'direccion','estado','ciudad','representante','telefono','correo']

        labels = {'proyecto':'Proyecto','estatus':'Estatus','nombre_centro':'Nombre del Centro', 'direccion':'Dirección','estado':'Estado','ciudad':'Ciudad','representante':'Representante','telefono':'Teléfono','correo':'Correo'}


class ExpProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['proyecto']

        labels = {'proyecto':'Seleccione el Proyecto'}


class JornadaForm(ModelForm):
    class Meta:
        model = Jornada
        fields = ['jornada','descripcion']

        labels = {'jornada':'Seleccione la Jornada','descripcion':'Descripción'}
        
        widgets = {'jornada': NumberInput(attrs={'type':'date'})}
