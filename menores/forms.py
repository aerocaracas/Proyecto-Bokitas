from django.forms import ModelForm
from django import forms
from bokitas.models import Menor, AntropMenor, Medica, Jornada, Vacunas
from django.forms.widgets import NumberInput 


SI_NO = (
    ("NO", "NO"),
    ("SI", "SI"),
)


class MenorForm(ModelForm):
    class Meta:
        model = Menor 
        fields = ['proyecto','jornada','parentesco','cedula','nombre','apellido','sexo','fecha_nac','fecha_ing_proyecto','observacion','estatus'
        ]

        labels = {'proyecto':'Proyecto','parentesco':'Parentesco','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','jornada':'Fecha de Jornada','fecha_ing_proyecto':'Fecha Ingreso','observacion':'Observación','estatus':'Estatus'
        }

        widgets = {
            'proyecto': forms.Select(attrs={"hx-get": "load_jornadas_menor/", "hx-target": "#id_jornada"}),
            'fecha_nac': NumberInput(attrs={'type':'date'}),
            'fecha_ing_proyecto': NumberInput(attrs={'type':'date'}),
            'observacion': forms.Textarea(attrs={'rows':4}),
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jornada'].queryset = Jornada.objects.none()

        if "proyecto" in self.data:
            proyecto_id = int(self.data.get("proyecto"))
            self.fields["jornada"].queryset = Jornada.objects.filter(proyecto_id=proyecto_id)
        elif self.instance.pk:
            self.fields['jornada'].queryset = self.instance.proyecto.jornada_set.order_by('jornada')


class ImcMenorForm(ModelForm):
    class Meta:
        model = AntropMenor 
        fields = ['jornada','peso','talla','cbi','ptr','pse','cc'
        ]

        labels = {'jornada':'Fecha Jornada','peso':'Peso','talla':'Talla','cbi':'CBI','ptr':'PTR','pse':'PSE','cc':'CC'
        }


class MedicaForm(forms.ModelForm):

    desp_familia = forms.ChoiceField(label='', choices=SI_NO, widget=forms.RadioSelect)
    desp_menor = forms.ChoiceField(label='', choices=SI_NO, widget=forms.RadioSelect)

    class Meta:
        model = Medica
        fields = ['jornada','medico_tratante','tipo_consulta','examen_fisico','diagnostico1','diagnostico2','diagnostico3','otros_varios','desp_menor','desp_familia','anemico','asesor_lactancia','recomen_nutricional','refe_psicologica','vitaminas','lacktokiana','prokids','tratamiento','referencia','paraclinicos'
        ]

        labels = {'jornada':'Fecha de Jornada','medico_tratante':'Medico Tratante','tipo_consulta':'Tipo de Consulta','examen_fisico':'Examen Fisico','diagnostico1':'','diagnostico2':'','diagnostico3':'','otros_varios':'Otro Diagnóstico','desp_menor':'Se encuentra el Paciente Desparacitado','desp_familia':'Se encuentra el Grupo Familiar Desparacitado','anemico':'', 'asesor_lactancia':'Asesoría en Lactancia', 'recomen_nutricional':'Recomendación Nutricional', 'refe_psicologica':'Referencia Psicológica', 'vitaminas':'Vitaminas', 'lacktokiana':'Lacktokiana', 'prokids':'Prokids', 'tratamiento':'Tratamiento Indicado','referencia':'Referencia','paraclinicos':'Paraclinicos Solicitados'
        }

        widgets = {
            'otros_varios': forms.Textarea(attrs={'rows':4}),
            'tratamiento': forms.Textarea(attrs={'rows':4}),
            'referencia': forms.Textarea(attrs={'rows':4}),
            'paraclinicos': forms.Textarea(attrs={'rows':4}),
                }
 

class VacunaForm(forms.ModelForm):

    class Meta:
        model = Vacunas
        fields = ['jornada','vacuna','dosis','observacion'
        ]

        labels = {'jornada':'Fecha de Jornada','vacuna':'Vacuna','dosis':'Dosis','observacion':'Observación'
        }

        widgets = {
            'observacion': forms.Textarea(attrs={'rows':4}),
                }
