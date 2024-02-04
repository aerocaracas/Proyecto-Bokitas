from django.contrib import admin
from .models import Centro
from .models import Beneficiario
from .models import Familiares
from .models import Menores
from .models import Antropometrico
from .models import Medica
from .models import Nutricional
from .models import Socioeconomico
from .models import Tareas
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
admin.site.register(Centro)
admin.site.register(Beneficiario)
admin.site.register(Familiares)
admin.site.register(Menores)
admin.site.register(Antropometrico)
admin.site.register(Medica)
admin.site.register(Nutricional)
admin.site.register(Socioeconomico)
admin.site.register(Tareas)
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
