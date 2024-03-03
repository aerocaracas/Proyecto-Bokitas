from django.forms import ModelForm
from bokitas.models import Medica

class MedicaForm(ModelForm):
    class Meta:
        model = Medica
        fields = '__all__'

