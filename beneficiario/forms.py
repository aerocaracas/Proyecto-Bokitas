from django.forms import ModelForm
from django import forms
from bokitas.models import Beneficiario, Familia, Menor, Medica
from django.forms.widgets import NumberInput 


SI_NO = (
    ("SI", "SI"),
    ("NO", "NO"),
)

SEXOS = (
    ("MASCULINO", "MASCULINO"),
    ("FEMENINO", "FEMENINO"),
)

DIAGNOSTICO1 = (
    ("Niño Sano", "Niño Sano"),
    ("Traumatismos varios", "Traumatismos varios"),
    ("Alérgia", "Alérgia"),
    ("Cefalea", "Cefalea"),
    ("Hiperreactividad bronquial y rinitis", "Hiperreactividad bronquial y rinitis"),
    )
DIAGNOSTICO2 = (    
    ("Infección respiratoria inferior", "Infección respiratoria inferior"),
    ("Faringoamigdalitis", "Faringoamigdalitis"),
    ("Sinusitis", "Sinusitis"),
    ("Parasitosis Intestinal", "Parasitosis Intestinal"),
    ("Diarreas", "Diarreas"),
    )
DIAGNOSTICO3 = (
    ("Dermatitis y otras afecciones de piel", "Dermatitis y otras afecciones de piel"),
    ("Otitis", "Otitis"),
    ("Caries dentales", "Caries dentales"),
    ("Abscesos dentales", "Abscesos dentales"),
)

ANEMICO = (
    ("Suplementación de Acido Folico", "Suplementación de Acido Folico"),
    ("Suplementación de Hierro", "Suplementación de Hierro"),
    ("Suplementación de Minerales y Vitaminas", "Suplementación de Minerales y Vitaminas"),
)

SI_NO = (
    ("SI", "SI"),
    ("NO", "NO"),
)

class BeneficiarioForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['proyecto','cedula','nombre','apellido','sexo', 'fecha_nac','embarazada','lactante','estado_civil','educacion','profesion','laboral','telefono','correo','direccion','estado','ciudad','observacion','estatus','numero_cuenta'
        ]

        labels = {'proyecto':'Proyecto','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo', 'fecha_nac':'Fecha de Nacimiento','embarazada':'Se encuentra Embarazada','lactante':'Se encuentra Lactando','estado_civil':'Estado Civil','educacion':'Educación','profesion':'Profesión','laboral':'Situación Laboral','telefono':'Teléfono','correo':'Correo Electrónico','direccion':'Dirección','estado':'Estado','ciudad':'Ciudad','observacion':'Observación','estatus':'Estatus','numero_cuenta':'Número de Cuenta'}

        widgets = {
            'fecha_nac': NumberInput(attrs={'type':'date'}),
            'direccion': forms.Textarea(attrs={'rows':3}),
            'observacion': forms.Textarea(attrs={'rows':3}),
                }

class MenorForm(ModelForm):
    class Meta:
        model = Menor 
        fields = ['proyecto','cedula','nombre','apellido','sexo','fecha_nac','fecha_ing_proyecto','observacion','estatus'
        ]

        labels = {'proyecto':'Proyecto','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','fecha_ing_proyecto':'Fecha Ingreso','observacion':'Observación','estatus':'Estatus'
        }

        widgets = {
            'fecha_nac': NumberInput(attrs={'type':'date'}),
            'fecha_ing_proyecto': NumberInput(attrs={'type':'date'}),
            'observacion': forms.Textarea(attrs={'rows':4}),
                }


class FamiliarForm(ModelForm):
    class Meta:
        model = Familia 
        fields = ['parentesco','cedula','nombre','apellido','sexo','fecha_nac','estado_civil','educacion','profesion','laboral','observacion'
        ]

        labels = {'cedula_bef':'Cédula Beneficiario','parentesco':'Parentesco','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','edad':'Edad','meses':'Meses','estado_civil':'Estado Civil','educacion':'Eduación','profesion':'Profesión','laboral':'Situación Laboral','observacion':'Observación'
        }

        widgets = {
            'observacion': forms.Textarea(attrs={'rows':4}),
            'fecha_nac': NumberInput(attrs={'type':'date'}),
                }


class MedicaForm(forms.ModelForm):

    desp_familia = forms.ChoiceField(label='', choices=SI_NO, widget=forms.RadioSelect)
    desp_menor = forms.ChoiceField(label='', choices=SI_NO, widget=forms.RadioSelect)

    class Meta:
        model = Medica
        fields = ['medico_tratante','tipo_consulta','examen_fisico','diagnostico1','diagnostico2','diagnostico3','otros_varios','desp_menor','desp_familia','anemico','tratamiento','referencia','paraclinicos'
        ]

        labels = {'medico_tratante':'Medico Tratante','tipo_consulta':'Tipo de Consulta','examen_fisico':'Examen Fisico','diagnostico1':'','diagnostico2':'','diagnostico3':'','otros_varios':'Otro Diagnóstico','desp_menor':'Se encuentra el Paciente Desparacitado','desp_familia':'Se encuentra el Grupo Familiar Desparacitado','anemico':'','tratamiento':'Tratamiento Indicado','referencia':'Referencia','paraclinicos':'Paraclinicos Solicitados'
        }

        widgets = {
            'otros_varios': forms.Textarea(attrs={'rows':4}),
            'tratamiento': forms.Textarea(attrs={'rows':4}),
            'referencia': forms.Textarea(attrs={'rows':4}),
            'paraclinicos': forms.Textarea(attrs={'rows':4}),
                }