from django.forms import ModelForm
from bokitas.models import Beneficiario, Familia, Menor, AntropMenor, Medicamento, Medica


class BeneficiarioForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['proyecto','cedula','nombre','apellido','sexo', 'fecha_nac','embarazada','lactando','estado_civil','educacion','profesion','laboral','telefono','correo','direccion','estado','ciudad','observacion','estatus','numero_cuenta'
        ]

        labels = {'proyecto':'Proyecto','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo', 'fecha_nac':'Fecha de Nacimiento','embarazada':'Se encuentra Embarazada','lactando':'Se encuentra Lactando','estado_civil':'Estado Civil','educacion':'Educación','profesion':'Profesión','laboral':'Situación Laboral','telefono':'Teléfono','correo':'Correo Electrónico','direccion':'Dirección','estado':'Estado','ciudad':'Ciudad','observacion':'Observación','estatus':'Estatus','numero_cuenta':'Número de Cuenta'}

        help_texts = {
            "fecha_nac":'dd/mm/aaaa'
        }

class MenorForm(ModelForm):
    class Meta:
        model = Menor 
        fields = ['proyecto','cedula','nombre','apellido','sexo','fecha_nac','fecha_ing_proyecto','observacion','estatus'
        ]

        labels = {'proyecto':'Proyecto','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','fecha_ing_proyecto':'Fecha Ingreso','observacion':'Observación','estatus':'Estatus'
        }

        help_texts = {
            "fecha_nac":'dd/mm/aaaa',"fecha_ing_proyecto":'dd/mm/aaaa'
        }


class FamiliarForm(ModelForm):
    class Meta:
        model = Familia 
        fields = ['parentesco','cedula','nombre','apellido','sexo','fecha_nac','estado_civil','educacion','profesion','laboral','observacion'
        ]

        labels = {'cedula_bef':'Cédula Beneficiario','parentesco':'Parentesco','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','edad':'Edad','meses':'Meses','estado_civil':'Estado Civil','educacion':'Eduación','profesion':'Profesión','laboral':'Situación Laboral','observacion':'Observación'
        }

        help_texts = {
            "fecha_nac":'dd/mm/aaaa'
        }

class MedicaForm(ModelForm):
    class Meta:
        model = Medica
        fields = '__all__'

