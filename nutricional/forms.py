from django.forms import ModelForm
from django import forms
from bokitas.models import Nutricional

SI_NO_MINUSCULA = (
    ("Si", "Si"),
    ("No", "No"),
)

class NutricionalForm(ModelForm):
    class Meta:
        model = Nutricional
        fields = "__all__"
        widgets = {
            'embarazada': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'lactante': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'frecuencia': forms.RadioSelect,
        }

