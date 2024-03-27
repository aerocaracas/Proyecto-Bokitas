from django.forms import ModelForm
from bokitas.models import Beneficiario, Familia, Menor, Antropometrico, Medicamento

class BeneficiarioForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['proyecto','cedula','nombre','apellido','sexo', 'fecha_nac','edad','meses','estado_civil','direccion','estado','ciudad','educacion','profesion','laboral','telefono','correo','embarazada','lactando','observacion','estatus','numero_cuenta'
        ]

        labels = {'proyecto':'Proyecto','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo', 'fecha_nac':'Fecha de Nacimiento','edad':'Edad','meses':'Meses','estado_civil':'Estado Civil','direccion':'Dirección','estado':'Estado','ciudad':'Ciudad','educacion':'Educación','profesion':'Profesión','laboral':'Situación Laboral','telefono':'Teléfono','correo':'Correo Electrónico','embarazada':'Se encuentra Embarazada','lactando':'Se encuentra Lactando','observacion':'Observación','estatus':'Estatus','numero_cuenta':'Número de Cuenta'}


class AntropBenefForm(ModelForm):
    class Meta:
        model = Antropometrico 
        fields = ['fecha','embarazo_lactando','tiempo_gestacion','peso','talla','cbi'
        ]

        labels = {'fecha':'Fecha','embarazo_lactando':'Embarazada / Lactando','tiempo_gestacion':'Tiempo','peso':'Peso','talla':'Talla','cbi':'CBI'
        }


class MenorForm(ModelForm):
    class Meta:
        model = Menor 
        fields = ['cedula_bef','proyecto','cedula','nombre','apellido','sexo','fecha_nac','edad','meses','fecha_ing_proyecto','observacion','estatus'
        ]

        labels = {'cedula_bef':'Cédula Beneficiario','proyecto':'Proyecto','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','edad':'Edad','meses':'Meses','fecha_ing_proyecto':'Fecha Ingreso','observacion':'Observación','estatus':'Estatus'
        }


class FamiliarForm(ModelForm):
    class Meta:
        model = Familia 
        fields = ['cedula_bef','parentesco','cedula','nombre','apellido','sexo','fecha_nac','edad','meses','estado_civil','educacion','profesion','laboral','observacion'
        ]

        labels = {'cedula_bef':'Cédula Beneficiario','parentesco':'Parentesco','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo','fecha_nac':'Fecha Nacimiento','edad':'Edad','meses':'Meses','estado_civil':'Estado Civil','educacion':'Eduación','profesion':'Profesión','laboral':'Situación Laboral','observacion':'Observación'
        }


class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['cedula_bef','fecha','nombre','descripcion','cantidad']

        labels = {'cedula_bef':'Cédula','fecha':'Fecha','nombre':'Nombre del Medicamento/Producto','descripcion':'Descripción','cantidad':'Cantidad'}