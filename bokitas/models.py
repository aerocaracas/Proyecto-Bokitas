from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from multiselectfield import MultiSelectField


# Specifying the choices
SEXOS = (
    ("MASCULINO", "MASCULINO"),
    ("FEMENINO", "FEMENINO"),
)

ESTADO_CIVIL = (
    ("SOLTERA", "SOLTERA"),
    ("SOLTERO", "SOLTERO"),
    ("CASADA", "CASADA"),
    ("CASADO", "CASADO"),
    ("DIVORCIADA", "DIVORCIADA"),
    ("DIVORCIADO", "DIVORCIADO"),
    ("VIUDA", "VIUDA"),
    ("VIUDO", "VIUDO"),
    ("CONCUBINATO", "CONCUBINATO"),
)

SI_NO = (
    ("SI", "SI"),
    ("NO", "NO"),
)

EDUCACION = (
    ("ANALFABETA", "ANALFABETA"),
    ("PRIMARIA", "PRIMARIA"),
    ("SECUNDARIA", "SECUNDARIA"),
    ("TECNICO MEDIO", "TECNICO MEDIO"),
    ("TECNICO SUPERIOR", "TECNICO SUPERIOR"),
    ("UNIVERSITARIO", "UNIVERSITARIO"),
)

LABORAL = (
    ("DESEMPLEADA", "DESEMPLEADA"),
    ("DESEMPLEADO", "DESEMPLEADO"),
    ("EMPLEADA", "EMPLEADA"),
    ("EMPLEADO", "EMPLEADO"),
    ("OCACIONAL", "OCACIONAL"),
    ("INDEPENDIENTE", "INDEPENDIENTE"),
)

ESTATUS = (
    ("ACTIVO", "ACTIVO"),
    ("CERRADO", "CERRADO"),
)

EMBARAZO_LACTANDO = (
    ("EMBARAZADA", "EMBARAZADA"),
    ("LACTANDO", "LACTANDO"),
)

HIJOS = (
    ("HIJO", "HIJO"),
    ("HIJA", "HIJA"),
)

PARENTESCO = (
    ("CONYUGUE", "CONYUGUE"),
    ("SOBRINO", "SOBRINO"),
    ("SOBRINA", "SOBRINA"),
    ("NIETO", "NIETO"),
    ("NIETA", "NIETA"),
    ("ASISTIDO", "ASISTIDO"),
    ("ASISTIDA", "ASISTIDA"),
    ("HERMANO", "HERMANO"),
    ("HERMANA", "HERMANA"),
    ("TIO", "TIO"),
    ("TIA", "TIA"),
    ("ABUELO", "ABUELO"),
    ("ABUELA", "ABUELA"),
)

TIPO_CONSULTA = (
    ("JORNADA", "JORNADA"),
    ("CONSULTA PROGRAMADA", "CONSULTA PROGRAMADA"),
    ("EMERGENCIA", "EMERGENCIA"),
)

EXAMEN_FISICO = (
    ("SANO", "SANO"),
    ("ANORMAL", "ANORMAL"),
)

DIAGNOSTICO1 = (
    ("Niño Sano", "Niño Sano"),
    ("Traumatismos varios", "Traumatismos varios"),
    ("Alérgia", "Alérgia"),
    ("Cefalea", "Cefalea"),
    ("Hiperreactividad bronquial y rinitis", "Hiperreactividad bronquial y rinitis"),
    )
DIAGNOSTICO2 = (    
    ("Infección respiratoria inferior", "Infección respiratoria inferior"),
    ("Faringoamigdalitis", "Faringoamigdalitis"),
    ("Sinusitis", "Sinusitis"),
    ("Parasitosis Intestinal", "Parasitosis Intestinal"),
    ("Diarreas", "Diarreas"),
    )
DIAGNOSTICO3 = (
    ("Dermatitis y otras afecciones de piel", "Dermatitis y otras afecciones de piel"),
    ("Otitis", "Otitis"),
    ("Caries dentales", "Caries dentales"),
    ("Abscesos dentales", "Abscesos dentales"),
)

ANEMICO = (
    ("Suplementación de Acido Folico", "Suplementación de Acido Folico"),
    ("Suplementación de Hierro", "Suplementación de Hierro"),
    ("Suplementación de Minerales y Vitaminas", "Suplementación de Minerales y Vitaminas"),
)



# Create your models here.
class Proyecto(models.Model):
    proyecto = models.CharField(max_length=100, unique=True, blank=False)
    estatus = models.CharField(max_length=10, blank=False, choices=ESTATUS)
    nombre_centro = models.CharField(max_length=50,blank=False)
    direccion = models.TextField(blank=True)
    estado = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=30)
    representante = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    correo = models.EmailField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('estatus',)

    def save(self, *args, **kwargs):
        self.proyecto = self.proyecto.upper()
        self.nombre_centro = self.nombre_centro.upper()
        self.representante = self.representante.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.proyecto}"

class Beneficiario(models.Model):
    cedula = models.CharField(max_length=15, unique=True, blank=False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=10, blank=False, choices=SEXOS)
    fecha_nac = models.DateField(null=False, blank=False)
    edad = models.PositiveIntegerField(default=0) 
    meses = models.PositiveIntegerField(default=0)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    direccion = models.TextField(blank=True)
    estado = models.CharField(max_length=25,blank=True)
    ciudad = models.CharField(max_length=30,blank=True)
    educacion = models.CharField(max_length=20, choices=EDUCACION,blank=True)
    profesion = models.CharField(max_length=25,blank=True)
    laboral = models.CharField(max_length=20, choices=LABORAL,blank=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(blank=True)
    embarazada = models.CharField(max_length=10, default="NO", choices=SI_NO)
    lactando = models.CharField(max_length=10, default="NO", choices=SI_NO)
    observacion = models.TextField(max_length=200, blank=True)
    estatus = models.CharField(max_length=10, default="ACTIVO", choices=ESTATUS)
    numero_cuenta = models.PositiveIntegerField(default=0,blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-cedula',)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.profesion = self.profesion.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cedula}, {self.nombre} {self.apellido}"

class Menor(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    cedula = models.CharField(max_length=15, unique=True, blank=False)
    parentesco = models.CharField(max_length=15,blank=False, choices=HIJOS)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=15,blank=False, choices=SEXOS)
    fecha_nac = models.DateField(null=False, blank=False)
    edad = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    fecha_ing_proyecto = models.DateField(null=True)
    observacion = models.TextField(max_length=200, blank=True)
    estatus = models.CharField(max_length=20,default=True, choices=ESTATUS)
    peso_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    talla_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    imc_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cbi_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ptr_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pse_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cc_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    diagnostico_actual = models.CharField(max_length=50, blank=False)
    diagnostico_talla_actual = models.CharField(max_length=50, blank=False)
    estado_nutri_actual = models.CharField(max_length=50, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-cedula_bef',)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.diagnostico_actual = self.diagnostico_actual.upper()
        self.diagnostico_talla_actual = self.diagnostico_talla_actual.upper()
        self.estado_nutri_actual = self.estado_nutri_actual.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cedula}, {self.nombre} {self.apellido},     {self.proyecto}"

class Familia(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=15, choices=PARENTESCO)
    cedula = models.CharField(max_length=15, unique=True, blank=False)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=20,null=False, blank=False, choices=SEXOS)
    fecha_nac = models.DateField(null=False, blank=False)
    edad = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    estado_civil = models.CharField(max_length=15, choices=ESTADO_CIVIL)
    educacion = models.CharField(max_length=20, choices=EDUCACION,blank=True)
    profesion = models.CharField(max_length=25,blank=True)
    laboral = models.CharField(max_length=20, choices=LABORAL,blank=True)
    observacion = models.TextField(max_length=200, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.profesion = self.profesion.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cedula}, {self.nombre} {self.apellido}"
    
    
class AntropMenor(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    cedula = models.ForeignKey(Familia, on_delete=models.CASCADE)
    proyecto = models.CharField(max_length=100, blank=False)
    fecha = models.DateTimeField(default=timezone.now)
    edad = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    talla = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cbi = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ptr = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pse = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cc = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    diagnostico = models.CharField(max_length=50, blank=False)
    diagnostico_talla = models.CharField(max_length=50, blank=False)
    riesgo = models.CharField(max_length=3,choices=SI_NO,default="NO")
    servicio = models.TextField(max_length=200, blank=True)
    centro_hospital = models.TextField(max_length=200, blank=True)
    observacion = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.cedula}, {self.cedula_bef} {self.proyecto}"

class AntropBef(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    embarazo_lactando = models.CharField(max_length=25,null=True, blank=True, choices=EMBARAZO_LACTANDO)
    tiempo_gestacion = models.PositiveIntegerField(default=0,null=True, blank=True,) 
    edad = models.PositiveIntegerField(default=0) 
    meses = models.PositiveIntegerField(default=0)
    peso = models.DecimalField(max_digits=5,decimal_places=2,default=0.00,help_text="Kg")
    talla = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    cbi = models.DecimalField(max_digits=5,decimal_places=2,default=0.00,blank=True,null=True)
    imc = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    diagnostico = models.CharField(max_length=50,blank=False)
    riesgo = models.CharField(max_length=3,choices=SI_NO,default="NO",blank=True,null=True)
    servicio = models.TextField(max_length=200,blank=True)
    centro_hospital = models.TextField(max_length=200,blank=True)
    observacion = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return f"{self.cedula_bef}"

class Medicamento(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    fecha = models.DateField()
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=100, blank=False)
    cantidad = models.CharField(max_length=50, blank=False)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cedula_bef}"


class Nutricional(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(auto_now_add=True)
    embarazada_ini = models.PositiveIntegerField()
    lactante_ini = models.PositiveIntegerField()
    gestacion = models.PositiveIntegerField()
    lactancia = models.PositiveIntegerField()
    mercado_padre = models.PositiveIntegerField()
    mercado_madre = models.PositiveIntegerField()
    mercado_abuelos = models.PositiveIntegerField()
    mercado_tios = models.PositiveIntegerField()
    mercado_otro = models.PositiveIntegerField()
    mercado = models.PositiveIntegerField()
    cocina_padre = models.PositiveIntegerField()
    cocina_madre = models.PositiveIntegerField()
    cocina_aduelos = models.PositiveIntegerField()
    cocina_tios = models.PositiveIntegerField()
    cocina_otro = models.PositiveIntegerField()
    cocina = models.PositiveIntegerField()
    frecuencia = models.PositiveIntegerField()
    apetito = models.PositiveIntegerField()
    cereales = models.PositiveIntegerField()
    vegetales = models.PositiveIntegerField()
    frutas = models.PositiveIntegerField()
    carnes = models.PositiveIntegerField()
    pollo = models.PositiveIntegerField()
    pescado = models.PositiveIntegerField()
    embutidos = models.PositiveIntegerField()
    viceras = models.PositiveIntegerField()
    grasas = models.PositiveIntegerField()
    lacteos = models.PositiveIntegerField()
    tuberculos = models.PositiveIntegerField()
    leguminosas = models.PositiveIntegerField()
    huevos = models.PositiveIntegerField()
    charcuteria = models.PositiveIntegerField()
    comidas = models.PositiveIntegerField()
    meriendas = models.PositiveIntegerField()
    grupos = models.PositiveIntegerField()
    grupo_cereales = models.PositiveIntegerField()
    grupo_frutas = models.PositiveIntegerField()
    grupo_leche = models.PositiveIntegerField()
    grupo_grasas = models.PositiveIntegerField()
    grupo_dulces = models.PositiveIntegerField()
    grupo_carnes = models.PositiveIntegerField()
    vegelales_rechazo = models.PositiveIntegerField()
    vegetales_prepararlo = models.PositiveIntegerField()
    vegetales_costo = models.PositiveIntegerField()
    vegetales_acostumbrado = models.PositiveIntegerField()
    frutas_rechazo = models.PositiveIntegerField()
    frutas_costosos = models.PositiveIntegerField()
    frutas_prepararlo = models.PositiveIntegerField()
    frutas_acostumbrado = models.PositiveIntegerField()
    viceras_rechazo = models.PositiveIntegerField()
    viceras_prepararlo = models.PositiveIntegerField()
    viceras_costosos = models.PositiveIntegerField()
    viceras_acostumbrado = models.PositiveIntegerField()
    bonos = models.PositiveIntegerField()
    bonos_entre = models.PositiveIntegerField()
    bono_entre6 = models.PositiveIntegerField()
    clap = models.PositiveIntegerField()
    clap_entre = models.PositiveIntegerField()
    clap_entre6 = models.PositiveIntegerField()
    iglesia = models.PositiveIntegerField()
    iglesia_entre = models.PositiveIntegerField()
    iglesia_entre6 = models.PositiveIntegerField()
    familiar = models.PositiveIntegerField()
    familiar_entre = models.PositiveIntegerField()
    familia_entre6 = models.PositiveIntegerField()
    pensionado = models.PositiveIntegerField()
    pensionado_entre = models.PositiveIntegerField()
    pensionado_entre6 = models.PositiveIntegerField()
    practica = models.PositiveIntegerField()
    tiempo = models.PositiveIntegerField()
    actividad = models.PositiveIntegerField()
    medicamento = models.PositiveIntegerField()
    medicamento_que = models.CharField(max_length=50, blank=True)
    agua_tuberia = models.PositiveIntegerField()
    agua_filtrada = models.PositiveIntegerField()
    agua_botellon = models.PositiveIntegerField()
    agua_hervida = models.PositiveIntegerField()
    agua_tableta = models.PositiveIntegerField()
    servicio_agua = models.PositiveIntegerField()
    servicio_electricidad = models.PositiveIntegerField() 
    servicio_telefono = models.PositiveIntegerField()
    servicio_aseo = models.PositiveIntegerField()
    servicio_no = models.PositiveIntegerField()
    compra_gas = models.PositiveIntegerField()
    compra_agua = models.PositiveIntegerField()
    almacena_agua = models.PositiveIntegerField()
    donde_almacena = models.PositiveIntegerField()
    conoce_grupos = models.PositiveIntegerField()
    conoce_calidad = models.PositiveIntegerField()
    conoce_desnutricion = models.PositiveIntegerField()
    desearia_conocimiento = models.PositiveIntegerField()
    conoce_beneficio = models.PositiveIntegerField()
    embarazada = models.PositiveIntegerField()
    lactando = models.PositiveIntegerField()
    desea_orientacion = models.PositiveIntegerField()
    frecuencia_alimentos = models.PositiveIntegerField()
    desea_amamantar = models.PositiveIntegerField()
    dificultad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cedula_bef}, {self.proyecto} {self.fecha}"

class Medica(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    cedula = models.ForeignKey(Menor, on_delete=models.CASCADE, blank=False)
    proyecto = models.CharField(max_length=50, blank=False)
    fecha = models.DateField(auto_now_add=True)
    edad = models.PositiveIntegerField(default=0) 
    meses = models.PositiveIntegerField(default=0)
    medico_tratante = models.CharField(max_length=50, blank=False)
    tipo_consulta = models.CharField(max_length=20, choices=TIPO_CONSULTA, blank=False)
    examen_fisico = models.CharField(max_length=10, choices=EXAMEN_FISICO, blank=False)
    diagnostico1 = MultiSelectField(max_length=200, choices=DIAGNOSTICO1, blank=True)
    diagnostico2 = MultiSelectField(max_length=200, choices=DIAGNOSTICO2, blank=True)
    diagnostico3 = MultiSelectField(max_length=200, choices=DIAGNOSTICO3, blank=True)
    otros_varios = models.TextField(max_length=200, blank=True)
    desp_menor = models.CharField(max_length=10,choices=SI_NO, blank=True)
    desp_familia = models.CharField(max_length=10,choices=SI_NO, blank=True)
    anemico = MultiSelectField(max_length=200, choices=ANEMICO, blank=True,null=False)
    tratamiento = models.TextField(max_length=200, blank=True)
    referencia = models.TextField(max_length=200, blank=True)
    paraclinicos = models.TextField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.medico_tratante = self.medico_tratante.upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cedula_bef}, {self.proyecto} {self.fecha}"

class Socioeconomico(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(auto_now_add=True)
    tipo_vivienda = models.PositiveIntegerField()
    material_vivienda = models.PositiveIntegerField()
    ambiente_vivienda = models.PositiveIntegerField()
    agua = models.PositiveIntegerField()
    agua_tiempo = models.PositiveIntegerField()
    alumbrado = models.PositiveIntegerField()
    barrido = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()
    seguridad = models.PositiveIntegerField()
    aseo = models.PositiveIntegerField()
    recreacion = models.PositiveIntegerField()
    porcentaje_servicio = models.PositiveIntegerField()
    basura = models.PositiveIntegerField()
    excreta = models.PositiveIntegerField()
    num_familia = models.PositiveIntegerField()
    genero = models.PositiveIntegerField()
    num_miembros = models.PositiveIntegerField()
    num_trabajando = models.PositiveIntegerField()
    num_hijos = models.PositiveIntegerField()
    tenencia_vivienda = models.PositiveIntegerField()
    profesion_jefe = models.PositiveIntegerField()
    nivel_instruccion = models.PositiveIntegerField()
    fuente_ingreso = models.PositiveIntegerField()
    estimado_ingreso = models.PositiveIntegerField()
    serv_telefono = models.PositiveIntegerField()
    serv_television = models.PositiveIntegerField()
    serv_bano = models.PositiveIntegerField()
    serv_computacion = models.PositiveIntegerField()
    serv_internet = models.PositiveIntegerField()
    serv_nevera = models.PositiveIntegerField()
    serv_lavadora = models.PositiveIntegerField()
    serv_secadora = models.PositiveIntegerField()
    serv_cocina = models.PositiveIntegerField()
    serv_microhonda = models.PositiveIntegerField()
    porcentaje_servicios = models.PositiveIntegerField()
    ambientes_dormitorios = models.PositiveIntegerField()
    indice_hacinamiento = models.PositiveIntegerField()
    indice_dependencia = models.PositiveIntegerField()
    resultado = models.PositiveIntegerField()
    clasificacion = models.PositiveIntegerField()
    observaciones = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.cedula_bef}, {self.proyecto} {self.fecha}"

class Estados(models.Model):
    id_estado = models.PositiveIntegerField()
    estado = models.CharField(max_length=40)
    iso_3166_2 = models.CharField(max_length=4)

class Ciudades(models.Model):
    id_ciudad = models.PositiveIntegerField()
    d_estado = models.PositiveIntegerField()
    Ciudad = models.CharField(max_length=40)
    capital = models.PositiveIntegerField()

class Diagnostico(models.Model):
    codigo_diag = models.PositiveIntegerField()
    diagnostico = models.CharField(max_length=25)

class ImcCla(models.Model):
    sexo = models.PositiveIntegerField()
    anos = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    l3sd = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    l2sd = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    l1sd = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    sd0 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    sd1 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    sd2 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    sd3 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

class ImcEmbarazada(models.Model):
    semana = models.PositiveIntegerField()
    p1 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p2 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p3 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p4 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p5 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p6 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

class ImcTalla(models.Model):
    sexo = models.PositiveIntegerField()
    anos = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    sd2_T = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd1_T = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd0 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

class ImcPesoTalla_5x(models.Model):
    edad = models.PositiveIntegerField(default=0)
    sexo = models.PositiveIntegerField()
    talla = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ds3_T = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ds2_T = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ds1_T = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ds0 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ds1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ds2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ds3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    completado = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo + ' - por ' + self.user.username
