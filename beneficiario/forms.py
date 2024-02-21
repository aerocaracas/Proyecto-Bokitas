from django.forms import ModelForm
from bokitas.models import Beneficiario

class BeneficiarioForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['proyecto','cedula','nombre','apellido','sexo', 'fecha_nac','edad','meses','estado_civil','direccion','estado','ciudad','educacion','profesion','laboral','telefono','correo','embarazada','lactando','condicion','estatus','numero_cuenta','tipo_usuario']

