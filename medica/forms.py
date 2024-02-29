from django.forms import ModelForm
from bokitas.models import Medica

class MedicaForm(ModelForm):
    class Meta:
        model = Medica
        fields = ['cedula_bef','cedula','proyecto','fecha','medico_tratante','tipo_consulta','examen_fisico','sano','traumatismo','alergia','cefalea','hiperactividad','infeccion','faringoamigdalitis','sinusitis','parasitosis','diarreas','dermatitis','otitis','caries','abcesos','otros','otros_varios','desp_menor','desp_familia','folico','cantidad_folico','hierro','cantidad_hierro','minerales','cantidad_minerales','vitamina','cantidad_vitamina','leche','cantidad_leche','antiviotico','cantidad_antiviotico','tratamiento','referencia','paraclinicos']

