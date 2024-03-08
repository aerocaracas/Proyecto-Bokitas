from django.forms import ModelForm
from bokitas.models import Beneficiario

class BeneficiarioForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['proyecto','cedula','nombre','apellido','sexo', 'fecha_nac','edad','meses','estado_civil','direccion','estado','ciudad','educacion','profesion','laboral','telefono','correo','embarazada','lactando','observacion','estatus','numero_cuenta']

        labels = {'proyecto':'Proyecto','cedula':'Cédula','nombre':'Nombre','apellido':'Apellido','sexo':'Sexo', 'fecha_nac':'Fecha de Nacimiento','edad':'Edad','meses':'Meses','estado_civil':'Estado Civil','direccion':'Dirección','estado':'Estado','ciudad':'Ciudad','educacion':'Educación','profesion':'Profesión','laboral':'Situación Laboral','telefono':'Teléfono','correo':'Correo Electrónico','embarazada':'Se encuentra Embarazada','lactando':'Se encuentra Lactando','observacion':'Observación','estatus':'Estatus','numero_cuenta':'Número de Cuenta'}

