from django.forms import ModelForm
from django import forms
from bokitas.models import Nutricional

SI_NO_MINUSCULA = (
    ("Si", "Si"),
    ("No", "No"),
)

FRECUENCIA = (
    ("Diario", "Diario"),
    ("2-3 días", "2-3 días"),
    ("Semanal", "Semanal"),
    ("Quincenal", "Quincenal"),
)

APETITO = (
    ("Bueno", "Bueno"),
    ("Regular", "Regular"),
    ("Malo", "Malo"),
    ("Elevado", "Elevado"),
)

COMIDAS = (
    ("1 Comida", "1 Comida"),
    ("2 Comidas", "2 Comidas"),
    ("3 Comidas", "3 Comidas"),
)

MERIENDA = (
    ("1 Merienda", "1 Merienda"),
    ("2 Meriendas", "2 Meriendas"),
    ("3 Meriendas", "3 Meriendas"),
    ("Ninguna", "Ninguna"),
)

GRUPOS = (
    ("1 - 2", "1 - 2"),
    ("2 - 3", "2 - 3"),
    ("3 - 4", "3 - 4"),
    ("4 - 5", "4 - 5"),
    ("5 - 6", "5 - 6"),
)

CONSUMO = (
    ("0/7", "0/7"),
    ("1-2/7", "1-2/7"),
    ("3-5/7", "3-5/7"),
    ("7/7", "7/7"),
    ("1-2/15", "1-2/15"),
    ("1-2/30", "1-2/30"),
)

TIEMPO = (
    ("30 min de 1-3 / 7", "30 min de 1-3 / 7"),
    ("30 min de 4-7 / 7", "30 min de 4-7 / 7"),
    ("más de 30 min 1-3 / 7", "más de 30 min 1-3 / 7"),
    ("más de 30 min 4-7 / 7", "más de 30 min 4-7 / 7"),
    ("No precisa datos", "No precisa datos"),
)

ACTIVIDAD = (
    ("Juegos Activos", "Juegos Activos"),
    ("Práctica Deportiva", "Práctica Deportiva"),
    ("Ambas Actividades", "Ambas Actividades"),
)

SI_NO_POCA = (
    ("Si", "Si"),
    ("No", "No"),
    ("Poca Información", "Poca Información"),
)

SI_NO_POCA_APLICA = (
    ("Si", "Si"),
    ("No", "No"),
    ("Poca Información ", "Poca Información "),
    ("No Aplica", "No Aplica"),
)


class NutricionalForm(ModelForm):
    class Meta:
        model = Nutricional
        fields = ['cedula_bef','embarazada','lactante','tiempo_gestacion','tiempo_lactancia','mercado_lorealiza','cocina_lorealiza','frecuencia','apetito','cuantas_comidas','meriendas','cuantos_grupos','tipo_grupos','cereales','vegetales','frutas','carnes','pollo','pescado','embutidos','viceras','grasas','lacteos','huevos','leguminosas','tuberculos','charcuteria','poco_vegetales','poco_frutas','poco_viceras','bonos','bonos_entre','clap','clap_entre','iglesia','iglesia_entre','familiar','familiar_entre','pensionado','pensionado_entre','practica_deporte','tiempo','actividad','medicamento','medicamento_suplemento','agua','falla_servicio','compra_gas','compra_agua','almacena_agua','donde_almacena','conoce_grupos','conoce_calidad','conoce_desnutricion','conoce_beneficio','embarazo','lactando','desea_amamantar','dificultad_amamantar','desea_orientacion','desea_conocimiento']

        labels = {'cedula_bef':'Cédula del Beneficiario','mercado_lorealiza':'Responsable de la compra en el mercado','frecuencia':'Frecuencia con que hace la compra','cocina_lorealiza':'Responsable de cocinar','apetito':'Cómo es su apetito?','cuantas_comidas':'Cuantas comidas realizan al día?','meriendas':'Cuantas meriendas?','cuantos_grupos':'Cuantos Grupos están presentes en su alimentación?','tipo_grupos':'Cuales son?','poco_vegetales':'El poco consumo o nada de Vegetales es:','poco_frutas':'El poco consumo o nada de Frutas es:','poco_viceras':'El poco consumo o nada de Viceras es:','practica_deporte':'Practica algún Deporte?','medicamento':'Consume algún Madicamento o Suplemento Nutricional?','medicamento_suplemento':'Qué Medicamento o Suplemento consume?','agua':'Cómo es el consumo de Agua?','falla_servicio':'Cual Servicio presenta fallas?','conoce_grupos':'Conoce los 5 a 6 Grupos de Alimentos?','conoce_calidad':'Conoce cómo mejorar la calidad de la proteina vegetal?','conoce_desnutricion':'Conoce sobre la desnutrición y su consecuencia?'}

        widgets = {
            'embarazada': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'lactante': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'frecuencia': forms.RadioSelect(choices=FRECUENCIA),
            'apetito': forms.RadioSelect(choices=APETITO),
            'cuantas_comidas': forms.RadioSelect(choices=COMIDAS),
            'meriendas': forms.RadioSelect(choices=MERIENDA),
            'cuantos_grupos': forms.RadioSelect(choices=GRUPOS),
            'cereales': forms.RadioSelect(choices=CONSUMO),
            'vegetales': forms.RadioSelect(choices=CONSUMO),
            'frutas': forms.RadioSelect(choices=CONSUMO),
            'carnes': forms.RadioSelect(choices=CONSUMO),
            'pollo': forms.RadioSelect(choices=CONSUMO),
            'pescado': forms.RadioSelect(choices=CONSUMO),
            'embutidos': forms.RadioSelect(choices=CONSUMO),
            'viceras': forms.RadioSelect(choices=CONSUMO),
            'grasas': forms.RadioSelect(choices=CONSUMO),
            'lacteos': forms.RadioSelect(choices=CONSUMO),
            'huevos': forms.RadioSelect(choices=CONSUMO),
            'leguminosas': forms.RadioSelect(choices=CONSUMO),
            'tuberculos': forms.RadioSelect(choices=CONSUMO),
            'charcuteria': forms.RadioSelect(choices=CONSUMO),
            'bonos': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'clap': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'iglesia': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'familiar': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'pensionado': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'practica_deporte': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'tiempo': forms.RadioSelect(choices=TIEMPO),
            'actividad': forms.RadioSelect(choices=ACTIVIDAD),
            'medicamento': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'medicamento_suplemento': forms.Textarea(attrs={'rows':3}),
            'compra_gas': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'compra_agua': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'almacena_agua': forms.RadioSelect(choices=SI_NO_MINUSCULA),
            'conoce_grupos': forms.RadioSelect(choices=SI_NO_POCA),
            'conoce_calidad': forms.RadioSelect(choices=SI_NO_POCA),
            'conoce_desnutricion': forms.RadioSelect(choices=SI_NO_POCA),
            'conoce_beneficio': forms.RadioSelect(choices=SI_NO_POCA_APLICA),
            'embarazo': forms.RadioSelect(choices=SI_NO_POCA_APLICA),
            'lactando': forms.RadioSelect(choices=SI_NO_POCA_APLICA),
            'desea_amamantar': forms.RadioSelect(choices=SI_NO_POCA_APLICA),
            'dificultad_amamantar': forms.RadioSelect(choices=SI_NO_POCA_APLICA),
            'desea_orientacion': forms.RadioSelect(choices=SI_NO_POCA_APLICA),
            'desea_conocimiento': forms.RadioSelect(choices=SI_NO_POCA_APLICA)
        }
