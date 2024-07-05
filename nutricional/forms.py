from django.forms import ModelForm
from django import forms
from bokitas.models import Nutricional


class NutricionalForm(ModelForm):
    class Meta:
        model = Nutricional
        fields = "__all__"

