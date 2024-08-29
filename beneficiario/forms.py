from django.forms import ModelForm
from django import forms
from bokitas.models import Beneficiario, Familia, Menor, AntropMenor, AntropBef, Medica, Jornada, Proyecto
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

class BeneficiarioForm(ModelForm):
    class Meta:
            model=Beneficiario

    proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.all(),
            widget=forms.Select(attrs={"hx-get": "load_jornadas_benef/", "hx-target": "#id_jornada"}))
    jornada = forms.ModelChoiceField(queryset=Jornada.objects.none())
    cedula = forms.CharField(label="Cédula")
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    sexo = forms.ChoiceField(choices=SEXOS,label="Sexo")
    fecha_nac = forms.DateField(label="Fecha Nacimiento", widget=forms.DateInput(attrs={'type':'date'}))
    nacionalidad = forms.CharField(label="Nacionalidad")
    num_hijos = forms.IntegerField(label="Numero de Hijos")
    embarazada = forms.ChoiceField(choices=SI_NO, label="Embarazada")
    lactante = forms.ChoiceField(choices=SI_NO, label="Lactando")
    estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL, label="Estado Civil")
    educacion = forms.ChoiceField(choices=EDUCACION, label="Educación")
    profesion = forms.CharField(label="Profesión")
    laboral = forms.ChoiceField(choices=LABORAL, label="Trabaja")
    telefono = forms.CharField(label="Telefono")
    correo = forms.EmailField(label="Correo")
    direccion = forms.CharField(label="Dirección", widget=forms.Textarea(attrs={'rows':3}))
    estado = forms.CharField(label="Estado")
    ciudad = forms.CharField(label="Ciudad")
    observacion = forms.CharField(label="Observación", widget=forms.Textarea(attrs={'rows':3}))
    estatus = forms.ChoiceField(choices=ESTATUS, label="Estatus")
    numero_cuenta = forms.CharField(label="Numero de Cuenta")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jornada'].queryset = Jornada.objects.none()

        if "proyecto" in self.data:
            proyecto_id = int(self.data.get("proyecto"))
            self.fields["jornada"].queryset = Jornada.objects.filter(proyecto_id=proyecto_id)





class ExpProyectoForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['proyecto']
        labels = {'proyecto':'Seleccione el Proyecto'}


class MenorForm(ModelForm):
    class Meta:
        model = Menor 
        fields = ['proyecto','jornada','parentesco','cedula','nombre','apellido','sexo','fecha_nac','fecha_ing_proyecto','observacion','estatus'
        ]

        labels = {'proyecto':'Proyecto','parentesco':'Parentesco','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','jornada':'Fecha de Jornada','fecha_ing_proyecto':'Fecha Ingreso','observacion':'Observación','estatus':'Estatus'
        }

        widgets = {
            'fecha_nac': NumberInput(attrs={'type':'date'}),
            'fecha_ing_proyecto': NumberInput(attrs={'type':'date'}),
            'observacion': forms.Textarea(attrs={'rows':4}),
                }


class ImcMenorForm(ModelForm):
    class Meta:
        model = AntropMenor 
        fields = ['jornada','peso','talla','cbi','ptr','pse','cc'
        ]

        labels = {'jornada':'Fecha Jornada','peso':'Peso','talla':'Talla','cbi':'CBI','ptr':'PTR','pse':'PSE','cc':'CC'
        }

        widgets = {
            'fecha': NumberInput(attrs={'type':'date'}),
                }


class ImcBenefForm(forms.Form):

    jornada = forms.ModelChoiceField(queryset=Jornada.objects.none())

    tiempo_gestacion = forms.IntegerField(label="Tiempo (meses)")
    peso = forms.DecimalField(label="Peso (kg)")
    talla = forms.DecimalField(label="Talla (cm)")
    cbi = forms.DecimalField(label="CBI")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jornada'].queryset = Jornada.objects.none()

        if "proyecto" in self.data:
            proyecto_id = int(self.data.get("proyecto"))
            self.fields["jornada"].queryset = Jornada.objects.filter(proyecto_id=proyecto_id)


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
        fields = ['jornada','medico_tratante','tipo_consulta','examen_fisico','diagnostico1','diagnostico2','diagnostico3','otros_varios','desp_menor','desp_familia','anemico','tratamiento','referencia','paraclinicos'
        ]

        labels = {'jornada':'Fecha de Jornada','medico_tratante':'Medico Tratante','tipo_consulta':'Tipo de Consulta','examen_fisico':'Examen Fisico','diagnostico1':'','diagnostico2':'','diagnostico3':'','otros_varios':'Otro Diagnóstico','desp_menor':'Se encuentra el Paciente Desparacitado','desp_familia':'Se encuentra el Grupo Familiar Desparacitado','anemico':'','tratamiento':'Tratamiento Indicado','referencia':'Referencia','paraclinicos':'Paraclinicos Solicitados'
        }

        widgets = {
            'otros_varios': forms.Textarea(attrs={'rows':4}),
            'tratamiento': forms.Textarea(attrs={'rows':4}),
            'referencia': forms.Textarea(attrs={'rows':4}),
            'paraclinicos': forms.Textarea(attrs={'rows':4}),
                }