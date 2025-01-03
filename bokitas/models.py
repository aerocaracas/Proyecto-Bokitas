from django.db import models
from django.contrib.auth.models import User
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
    ("ALTA", "ALTA"),
    ("EGRESO", "EGRESO"),
    ("DESINCORPORADO", "DESINCORPORADO"),
    ("CERRADO", "CERRADO"),
)

EMBARAZO_LACTANDO = (
    ("EMBARAZADA", "EMBARAZADA"),
    ("LACTANDO", "LACTANDO"),
)

HIJOS = (
    ("HIJO", "HIJO"),
    ("HIJA", "HIJA"),
    ("SOBRINO", "SOBRINO"),
    ("SOBRINA", "SOBRINA"),
    ("NIETO", "NIETO"),
    ("NIETA", "NIETA"),
    ("ASISTIDO", "ASISTIDO"),
    ("ASISTIDA", "ASISTIDA"),
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

MERCADO = (
    ("Padre", "Padre"),
    ("Madre", "Madre"),
    ("Abuelo(a)", "Abuelo(a)"),
    ("Tio(a)", "Tio(a)"),
    ("Otros", "Otros"),
)

TIPO_GRUPOS = (
    ("Cereales y Leguminosas", "Cereales y Leguminosas"),
    ("Frutas y Verduras", "Frutas y Verduras"),
    ("Leche Yogures y Quesos", "Leche Yogures y Quesos"),
    ("Grasas y Aceites", "Grasas y Aceites"),
    ("Dulces", "Dulces"),
    ("Carnes y Huevos", "Carnes y Huevos"),
)

POCO_CONSUMO = (
    ("Por Rechazo", "Por Rechazo"),
    ("No sabe prepararlo", "No sabe prepararlo"),
    ("Están muy costosos", "Están muy costosos"),
    ("No están acostumbrados", "No están acostumbrados"),
)

ENTRE = (
    ("Entre 1 a 3 meses", "Entre 1 a 3 meses"),
    ("Entre 3 a 6 meses", "Entre 3 a 6 meses"),
)

AGUA = (
    ("Tuberia sin Tratamiento", "Tuberia sin Tratamiento"),
    ("Filtrada", "Filtrada"),
    ("Botellon", "Botellon"),
    ("Hervida", "Hervida"),
    ("Tabletas Aguatab", "Tabletas Aguatab"),
)

FALLA = (
    ("Agua", "Agua"),
    ("Gas", "Gas"),
    ("Eléctricidad", "Eléctricidad"),
    ("Telefonía Internet", "Telefonía Internet"),
    ("Aseo Urbano", "Aseo Urbano"),
)

ALMACENA = (
    ("Pipote", "Pipote"),
    ("Tanque", "Tanque"),
    ("Otros", "Otros"),
)

SI_NO_MINUSCULA = (
    ("Si", "Si"),
    ("No", "No"),
)

VACUNAS = (
    ("Anti Tuberculosis - BCG", "Anti Tuberculosis - BCG"),
    ("Anti Hepatitis B - HB", "Anti Hepatitis B - HB"),
    ("Anti Poliomielitis - VPI-bVPO", "Anti Poliomielitis - VPI-bVPO"),
    ("Anti Difteria, Tétano y Pertussis - DTPc-DTPa", "Anti Difteria, Tétano y Pertussis - DTPc-DTPa"),
    ("Anti Haemophilus Influenzae Tipo B - Hib", "Anti Haemophilus Influenzae Tipo B - Hib"),
    ("Antirrotavirus - RV1-RV5", "Antirrotavirus - RV1-RV5"),
    ("Anti Streptococus Pneumoniae I0 o I3 V - VCN", "Anti Streptococus Pneumoniae I0 o I3 V - VCN"),
    ("Anti Influenza", "Anti Influenza"),
    ("Anti SRS - SRP1-2", "Anti SRS - SRP1-2"),
    ("Anti Amarílica - FA", "Anti Amarílica - FA"),
    ("Anti Hepatitis A - HA", "Anti Hepatitis A - HA"),
    ("Anti Varicela", "Anti Varicela"),
    ("Anti meningococo conjugada A,C,Y,W-135", "Anti meningococo conjugada A,C,Y,W-135"),
    ("Anti Streptococcus Pneumoniae 23V", "Anti Streptococcus Pneumoniae 23V"),

)

DOSIS_VACUNAS = (
    ("1ra DOSIS", "1ra DOSIS"),
    ("2da DOSIS", "2da DOSIS"),
    ("3ra DOSIS", "3ra DOSIS"),
    ("4ta DOSIS", "4ta DOSIS"),
    ("5ta DOSIS", "5ta DOSIS"),
    ("REFUERZO 1ra DOSIS", "REFUERZO 1ra DOSIS"),
    ("REFUERZO 2da DOSIS", "REFUERZO 2da DOSIS"),
    ("REFUERZO 3ra DOSIS", "REFUERZO 3ra DOSIS"),
)

# Create your models here.
class Proyecto(models.Model):
    proyecto = models.CharField(max_length=100, unique=True, blank=False)
    estatus = models.CharField(max_length=30, blank=False, choices=ESTATUS)
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
    

class Jornada(models.Model):
    jornada = models.DateField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ('jornada',)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.jornada}, {self.proyecto}"


class Beneficiario(models.Model):
    cedula = models.PositiveIntegerField(default=0, unique=True, blank=False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=10, blank=False, choices=SEXOS)
    fecha_nac = models.DateField(null=True, blank=True)
    edad = models.PositiveIntegerField(default=0) 
    meses = models.PositiveIntegerField(default=0)
    nacionalidad = models.CharField(max_length=100, blank=True)
    num_hijos = models.IntegerField(default=0) 
    embarazada = models.CharField(max_length=10, default="NO", choices=SI_NO)
    lactante = models.CharField(max_length=10, default="NO", choices=SI_NO)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    educacion = models.CharField(max_length=20, choices=EDUCACION,blank=True)
    profesion = models.CharField(max_length=25,blank=True)
    laboral = models.CharField(max_length=20, choices=LABORAL,blank=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(blank=True)
    direccion = models.CharField(max_length=200,blank=True)
    estado = models.CharField(max_length=25,blank=True)
    ciudad = models.CharField(max_length=30,blank=True)
    estatus = models.CharField(max_length=30, default="ACTIVO", choices=ESTATUS)
    numero_cuenta = models.CharField(max_length=20,blank=True)
    observacion = models.CharField(max_length=200, blank=True)
    creado = models.DateField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-cedula',)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.nacionalidad = self.nacionalidad.upper()
        self.profesion = self.profesion.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cedula}, {self.nombre} {self.apellido}"


class Menor(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
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
    estatus = models.CharField(max_length=30,default=True, choices=ESTATUS)
    peso_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    talla_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    imc_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cbi_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ptr_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pse_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cc_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    diagnostico_inicial = models.CharField(max_length=50, blank=True)
    diagnostico_talla_inicial = models.CharField(max_length=50, blank=True)
    peso_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    talla_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    imc_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cbi_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ptr_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pse_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cc_actual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    diagnostico_actual = models.CharField(max_length=50, blank=True)
    diagnostico_talla_actual = models.CharField(max_length=50, blank=False)
    estado_nutri_actual = models.CharField(max_length=50, blank=False)
    creado = models.DateField(auto_now_add=True)
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
    cedula = models.ForeignKey(Menor, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    edad = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    talla = models.DecimalField(max_digits=5, decimal_places=2)
    cbi = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ptr = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,default=0.00)
    pse = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,default=0.00)
    cc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,default=0.00)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    diagnostico = models.CharField(max_length=50, blank=False)
    diagnostico_talla = models.CharField(max_length=50, blank=False)
    riesgo = models.CharField(max_length=3,choices=SI_NO,default="NO")
    servicio = models.TextField(max_length=200, blank=True)
    centro_hospital = models.TextField(max_length=200, blank=True)
    observacion = models.TextField(max_length=200, blank=True)
    creado = models.DateField(auto_now_add=True)
    min_peso = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    max_peso = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    min_talla = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    max_talla = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    min_imc = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    max_imc = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.cedula}, {self.cedula_bef} {self.proyecto}"


class AntropBef(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    embarazo_lactando = models.CharField(max_length=25,null=True, blank=True, choices=EMBARAZO_LACTANDO)
    tiempo_gestacion = models.PositiveIntegerField(default=0) 
    edad = models.PositiveIntegerField(default=0) 
    meses = models.PositiveIntegerField(default=0)
    peso = models.DecimalField(max_digits=5,decimal_places=2,help_text="Kg")
    talla = models.DecimalField(max_digits=5,decimal_places=2,help_text="cm")
    cbi = models.DecimalField(max_digits=5,decimal_places=2,default=0.00,blank=True,null=True,help_text="cm")
    imc = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    diagnostico = models.CharField(max_length=50,blank=False)
    riesgo = models.CharField(max_length=3,choices=SI_NO,default="NO",blank=True,null=True)
    servicio = models.TextField(max_length=200,blank=True)
    centro_hospital = models.TextField(max_length=200,blank=True)
    observacion = models.TextField(max_length=200,blank=True)
    creado = models.DateField(auto_now_add=True)
    min_imc = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    max_imc = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.cedula_bef}"


class Medicamento(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=100, blank=False)
    cantidad = models.IntegerField()
    creado = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cedula_bef}"


class Nutricional(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    en_embarazo = models.CharField(max_length=10, blank=True)
    en_lactando = models.CharField(max_length=10, blank=True)
    tiempo_gestacion = models.PositiveIntegerField(default=0,null=True, blank=True,) 
    tiempo_lactancia = models.PositiveIntegerField(default=0,null=True, blank=True,) 
    mercado_lorealiza = MultiSelectField(max_length=200, choices=MERCADO, blank=True)
    cocina_lorealiza = MultiSelectField(max_length=200, choices=MERCADO, blank=True)
    frecuencia = models.CharField(max_length=10, blank=True)
    apetito = models.CharField(max_length=10, blank=True)
    cuantas_comidas = models.CharField(max_length=10, blank=True)
    meriendas = models.CharField(max_length=100, blank=True)
    cuantos_grupos = models.CharField(max_length=10, blank=True)
    tipo_grupos = MultiSelectField(max_length=200, choices=TIPO_GRUPOS, blank=True)
    cereales = models.CharField(max_length=12, blank=True)
    vegetales = models.CharField(max_length=12, blank=True)
    frutas = models.CharField(max_length=12, blank=True)
    carnes = models.CharField(max_length=12, blank=True)
    pollo = models.CharField(max_length=12, blank=True)
    pescado = models.CharField(max_length=12, blank=True)
    embutidos = models.CharField(max_length=12, blank=True)
    viceras = models.CharField(max_length=12, blank=True)
    grasas = models.CharField(max_length=12, blank=True)
    lacteos = models.CharField(max_length=12, blank=True)
    huevos = models.CharField(max_length=12, blank=True)
    leguminosas = models.CharField(max_length=12, blank=True)
    tuberculos = models.CharField(max_length=12, blank=True)
    charcuteria = models.CharField(max_length=12, blank=True)
    poco_vegetales = MultiSelectField(max_length=200, choices=POCO_CONSUMO, blank=True)
    poco_frutas = MultiSelectField(max_length=200, choices=POCO_CONSUMO, blank=True)
    poco_viceras = MultiSelectField(max_length=200, choices=POCO_CONSUMO, blank=True)
    bonos = models.CharField(max_length=10, blank=True)
    bonos_entre = models.CharField(max_length=50, blank=True)
    clap = models.CharField(max_length=10, blank=True)
    clap_entre = models.CharField(max_length=50, blank=True)
    iglesia = models.CharField(max_length=10, blank=True)
    iglesia_entre = models.CharField(max_length=50, blank=True)
    familiar = models.CharField(max_length=10, blank=True)
    familiar_entre = models.CharField(max_length=50, blank=True)
    pensionado = models.CharField(max_length=10, blank=True)
    pensionado_entre = models.CharField(max_length=50, blank=True)
    practica_deporte = models.CharField(max_length=10, blank=True)
    tiempo = models.CharField(max_length=100, blank=True)
    actividad = models.CharField(max_length=100, blank=True)
    medicamento = models.CharField(max_length=10, blank=True)
    medicamento_suplemento = models.TextField(max_length=150, blank=True)
    agua = MultiSelectField(max_length=200, choices=AGUA, blank=True)
    falla_servicio = MultiSelectField(max_length=200, choices=FALLA, blank=True)
    compra_gas = models.CharField(max_length=10, blank=True)
    compra_agua = models.CharField(max_length=10, blank=True)
    almacena_agua = models.CharField(max_length=10, blank=True)
    donde_almacena = MultiSelectField(max_length=200, choices=ALMACENA, blank=True)
    conoce_grupos = models.CharField(max_length=50, blank=True)
    conoce_calidad = models.CharField(max_length=50, blank=True)
    conoce_desnutricion = models.CharField(max_length=50, blank=True)
    conoce_beneficio = models.CharField(max_length=50, blank=True)
    embarazo = models.CharField(max_length=100, blank=True)
    lactando = models.CharField(max_length=100, blank=True)
    desea_amamantar = models.CharField(max_length=100, blank=True)
    dificultad_amamantar = models.CharField(max_length=100, blank=True)
    desea_orientacion = models.CharField(max_length=100, blank=True)
    desea_conocimiento = models.CharField(max_length=100, blank=True)
    creado = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.cedula_bef}"


class Medica(models.Model):
    cedula_bef = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    cedula = models.ForeignKey(Menor, on_delete=models.CASCADE, blank=False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    edad = models.PositiveIntegerField(default=0) 
    meses = models.PositiveIntegerField(default=0)
    medico_tratante = models.CharField(max_length=50, blank=False)
    tipo_consulta = models.CharField(max_length=20, choices=TIPO_CONSULTA, blank=False)
    examen_fisico = models.CharField(max_length=10, choices=EXAMEN_FISICO, blank=False)
    sano = models.BooleanField(default=False)
    traumatismo = models.BooleanField(default=False)
    alergia = models.BooleanField(default=False)
    cefalea = models.BooleanField(default=False)
    rinitis = models.BooleanField(default=False)
    infeccion = models.BooleanField(default=False)
    faringoamigdalitis = models.BooleanField(default=False)
    sinusitis = models.BooleanField(default=False)
    parasitosis = models.BooleanField(default=False)
    diarreas = models.BooleanField(default=False)
    dermatitis = models.BooleanField(default=False)
    otitis = models.BooleanField(default=False)
    caries = models.BooleanField(default=False)
    abscesos = models.BooleanField(default=False)
    otros_varios = models.TextField(max_length=200, blank=True)
    desp_menor = models.CharField(max_length=10,choices=SI_NO, blank=True)
    desp_familia = models.CharField(max_length=10,choices=SI_NO, blank=True)
    folico = models.BooleanField(default=False)
    hierro = models.BooleanField(default=False)
    minerales = models.BooleanField(default=False)
    asesor_lactancia = models.BooleanField(default=False)
    recomen_nutricional = models.BooleanField(default=False)
    refe_psicologica = models.BooleanField(default=False)
    vitaminas = models.BooleanField(default=False)
    lacktokiana = models.BooleanField(default=False)
    prokids = models.BooleanField(default=False)
    tratamiento = models.TextField(max_length=200, blank=True)
    referencia = models.TextField(max_length=200, blank=True)
    paraclinicos = models.TextField(max_length=200, blank=True)
    creado = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.medico_tratante = self.medico_tratante.upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cedula_bef}, {self.proyecto} {self.fecha}"
    

class Vacunas(models.Model):
    cedula = models.ForeignKey(Menor, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    vacuna = models.CharField(max_length=50, choices=VACUNAS, blank=False)
    dosis = models.CharField(max_length=50, choices=DOSIS_VACUNAS, blank=False)
    edad = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    observacion = models.TextField(max_length=200, blank=True)
    creado = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cedula}"


class Diagnostico(models.Model):
    codigo_diag = models.PositiveIntegerField()
    diagnostico = models.CharField(max_length=25)
    color1 = models.CharField(max_length=10)
    color2 = models.CharField(max_length=10)
    color3 = models.CharField(max_length=10)
    color4 = models.CharField(max_length=10)
    color5 = models.CharField(max_length=10)


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
    p2 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p3 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p4 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    p5 = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)


class ImcTalla(models.Model):
    sexo = models.PositiveIntegerField()
    anos = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    sd2_T = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd1_T = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd0 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sd2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)


class ImcCla_5x(models.Model):
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
    title = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo + ' - por ' + self.user.username
