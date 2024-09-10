from django.forms import ModelForm
from django import forms
from bokitas.models import Beneficiario, Familia, AntropBef, Jornada, Medicamento
from django.forms.widgets import NumberInput 


SI_NO = (
    ("SI", "SI"),
    ("NO", "NO"),
)

SEXOS = (
    ("FEMENINO", "FEMENINO"),
    ("MASCULINO", "MASCULINO"),
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
    ("NO", "NO"),
    ("SI", "SI"),
)

ESTADO_CIVIL = (
    ("SOLTERA", "SOLTERA"),
    ("SOLTERO", "SOLTERO"),
    ("CASADA", "CASADA"),
    ("CASADO", "CASADO"),
    ("DIVORCIADA", "DIVORCIADA"),
    ("DIVORCIADO", "DIVORCIADO"),
    ("VIUDA", "VIUDA"),
    ("VIUDO", "VIUDO"),
    ("CONCUBINATO", "CONCUBINATO"),
)

EDUCACION = (
    ("ANALFABETA", "ANALFABETA"),
    ("PRIMARIA", "PRIMARIA"),
    ("SECUNDARIA", "SECUNDARIA"),
    ("TECNICO MEDIO", "TECNICO MEDIO"),
    ("TECNICO SUPERIOR", "TECNICO SUPERIOR"),
    ("UNIVERSITARIO", "UNIVERSITARIO"),
)

LABORAL = (
    ("DESEMPLEADA", "DESEMPLEADA"),
    ("DESEMPLEADO", "DESEMPLEADO"),
    ("EMPLEADA", "EMPLEADA"),
    ("EMPLEADO", "EMPLEADO"),
    ("OCACIONAL", "OCACIONAL"),
    ("INDEPENDIENTE", "INDEPENDIENTE"),
)

ESTATUS = (
    ("ACTIVO", "ACTIVO"),
    ("CERRADO", "CERRADO"),
    ("EGRESO", "EGRESO"),
    ("DESINCORPORACION", "DESINCORPORACION"),
)

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario 
    
        fields = ['proyecto','jornada','cedula','nombre','apellido','sexo','fecha_nac','nacionalidad','num_hijos','embarazada','lactante','estado_civil','educacion','profesion','laboral','telefono','correo','direccion','ciudad','estado','observacion','estatus','numero_cuenta'
        ]

        labels = {'proyecto':'Proyecto','jornada':'Fecha de Jornada','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','nacionalidad':'Nacionalidad','num_hijos':'Número Hijos','embarazada':'Embarazada','lactando':'Lactando','estado_civil':'Estado Civil','educacion':'Grado de Instrucción','profesion':'Profesión','laboral':'Estado Laboral','telefono':'Teléfono','correo':'Correo','direccion':'Dirección','ciudad':'Ciudad','estado':'Estado','observacion':'Observación','estatus':'Estatus','num_cuenta':'Número de Cuenta'
        }

        widgets = {
            'proyecto': forms.Select(attrs={"hx-get": "load_jornadas_benef/", "hx-target": "#id_jornada"}),
            'fecha_nac': NumberInput(attrs={'type':'date'}),
            'direccion': forms.Textarea(attrs={'rows':4}),
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


class ExpProyectoForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['proyecto']
        labels = {'proyecto':'Seleccione el Proyecto'}


class ImcBenefForm(ModelForm):
    class Meta:
        model = AntropBef
        fields = ['jornada','tiempo_gestacion','peso','talla','cbi'
        ]

        labels = {'jornada':'Fecha Jornada','peso':'Peso','talla':'Talla','cbi':'CBI'
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


class MedicamentosForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['jornada','nombre','descripcion','cantidad'
        ]

        labels = {'jornada':'Fecha Jornada','nombre':'Nombre del Medicamento/Producto','descripcion':'Descripción','cantidad':'Cantidad'
        }