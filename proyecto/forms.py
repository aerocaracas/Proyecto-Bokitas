from django import forms
from bokitas.models import Proyecto,Jornada 
from django.forms.widgets import NumberInput


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['proyecto','estatus','nombre_centro', 'direccion','estado','ciudad','representante','telefono','correo']

        labels = {'proyecto':'Proyecto','estatus':'Estatus','nombre_centro':'Nombre del Centro', 'direccion':'Dirección','estado':'Estado','ciudad':'Ciudad','representante':'Representante','telefono':'Teléfono','correo':'Correo'}


class ExpProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['proyecto']

        labels = {'proyecto':'Seleccione el Proyecto'}


class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = ['jornada','descripcion']

        labels = {'jornada':'Seleccione la Jornada','descripcion':'Descripción'}
        
        widgets = {'jornada': NumberInput(attrs={'type':'date'})}


class ExpJornadaForm(forms.Form):
    proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.all(),
            widget=forms.Select(attrs={"hx-get": "load_jornadas/", "hx-target": "#id_jornada"}))
    jornada = forms.ModelChoiceField(queryset=Jornada.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jornada'].queryset = Jornada.objects.none()

        if "proyecto" in self.data:
            proyecto_id = int(self.data.get("proyecto"))
            self.fields["jornada"].queryset = Jornada.objects.filter(proyecto_id=proyecto_id)



