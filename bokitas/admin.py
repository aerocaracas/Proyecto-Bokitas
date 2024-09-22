from django.contrib import admin
from .models import Proyecto
from .models import Beneficiario
from .models import Familia
from .models import Menor
from .models import AntropMenor
from .models import AntropBef
from .models import Medica
from .models import Medicamento
from .models import Nutricional
from .models import Vacunas
from .models import Tarea
from .models import Diagnostico
from .models import ImcCla
from .models import ImcCla_5x
from .models import ImcEmbarazada
from .models import ImcPesoTalla_5x
from .models import ImcTalla
from .models import Jornada


# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Beneficiario)
admin.site.register(Familia)
admin.site.register(Menor)
admin.site.register(AntropMenor)
admin.site.register(AntropBef)
admin.site.register(Medica)
admin.site.register(Medicamento)
admin.site.register(Nutricional)
admin.site.register(Vacunas)
admin.site.register(Tarea)
admin.site.register(Diagnostico)
admin.site.register(ImcCla)
admin.site.register(ImcCla_5x)
admin.site.register(ImcEmbarazada)
admin.site.register(ImcPesoTalla_5x)
admin.site.register(ImcTalla)
admin.site.register(Jornada)


