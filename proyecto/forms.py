from django import forms
from bokitas.models import Proyecto,Jornada 
from django.forms.widgets import NumberInput
from django.views.generic import FormView 

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



class ExpJornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = ('proyecto','jornada')

        labels = {'proyecto':'Seleccione el Proyecto','jornada':'Seleccione la Jornada'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jornada'].queryset = Jornada.objects.none()

        if 'proyecto' in self.data:
            try:
                proyecto_value = self.data.get('proyecto')
                self.fields['jornada'].queryset = Jornada.objects.filter(proyecto_id=proyecto_value)
                print(self.fields['jornada'].queryset)
            except (ValueError, TypeError):
                pass

    def clean_jornada(self):
        jornada_value = self.cleaned_data.get('jornada')
        if not jornada_value:
            raise ExpJornadaForm.ValidationError('Debe seleccionar un valor para la Jornada')
        return jornada_value
    

class EditarFormView(FormView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['jornada'] = self.request.GET.get('jornada')
        return kwargs




class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = ['jornada','descripcion']

        labels = {'jornada':'Seleccione la Jornada','descripcion':'Descripción'}
        
        widgets = {'jornada': NumberInput(attrs={'type':'date'})}
