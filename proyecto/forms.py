from django.forms import ModelForm
from bokitas.models import Proyecto,Jornada, Beneficiario
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


class ExpJornadaForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(ExpJornadaForm, self).__init__(*args, **kwargs)
            self.fields['jornada'].queryset = Jornada.objects.filter(proyecto_id = self.instance.proyecto)

    class Meta:
        model = Beneficiario
        fields = ['proyecto','jornada']
        labels = {'proyecto':'Seleccione el Proyecto','jornada':'Seleccione la Jornada'}



class JornadaForm(ModelForm):
    class Meta:
        model = Jornada
        fields = ['jornada','descripcion']

        labels = {'jornada':'Seleccione la Jornada','descripcion':'Descripción'}
        
        widgets = {'jornada': NumberInput(attrs={'type':'date'})}
