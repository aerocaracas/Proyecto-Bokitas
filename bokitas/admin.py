from django.contrib import admin
from .models import Proyecto
from .models import Beneficiario
from .models import Familia
from .models import Menor
from .models import Antropometrico
from .models import Medica
from .models import Medicamento
from .models import Nutricional
from .models import Socioeconomico
from .models import Tarea
from .models import Diagnostico
from .models import Imc
from .models import ImcCla
from .models import ImcEmbarazada
from .models import ImcPesoTalla_5x
from .models import ImcTalla
from .models import Estados
from .models import Municipios
from .models import Ciudades
from .models import Parroquias

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Beneficiario)
admin.site.register(Familia)
admin.site.register(Menor)
admin.site.register(Antropometrico)
admin.site.register(Medica)
admin.site.register(Medicamento)
admin.site.register(Nutricional)
admin.site.register(Socioeconomico)
admin.site.register(Tarea)
admin.site.register(Diagnostico)
admin.site.register(Imc)
admin.site.register(ImcCla)
admin.site.register(ImcEmbarazada)
admin.site.register(ImcPesoTalla_5x)
admin.site.register(ImcTalla)
admin.site.register(Estados)
admin.site.register(Municipios)
admin.site.register(Ciudades)
admin.site.register(Parroquias)
