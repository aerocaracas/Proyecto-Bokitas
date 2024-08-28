# Generated by Django 5.0.3 on 2024-08-28 19:02

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_diag', models.PositiveIntegerField()),
                ('diagnostico', models.CharField(max_length=25)),
                ('color1', models.CharField(max_length=10)),
                ('color2', models.CharField(max_length=10)),
                ('color3', models.CharField(max_length=10)),
                ('color4', models.CharField(max_length=10)),
                ('color5', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ImcCla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.PositiveIntegerField()),
                ('anos', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('l3sd', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('l2sd', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('l1sd', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd0', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd1', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd2', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd3', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='ImcCla_5x',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.PositiveIntegerField()),
                ('anos', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('l3sd', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('l2sd', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('l1sd', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd0', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd1', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd2', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sd3', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='ImcEmbarazada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.PositiveIntegerField()),
                ('p2', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('p3', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('p4', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('p5', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='ImcPesoTalla_5x',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.PositiveIntegerField(default=0)),
                ('sexo', models.PositiveIntegerField()),
                ('talla', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ds3_T', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ds2_T', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ds1_T', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ds0', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ds1', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ds2', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ds3', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ImcTalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.PositiveIntegerField()),
                ('anos', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('sd2_T', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sd1_T', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sd0', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sd1', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sd2', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jornada', models.DateField()),
                ('descripcion', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('jornada',),
            },
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], max_length=10)),
                ('fecha_nac', models.DateField()),
                ('edad', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('nacionalidad', models.CharField(blank=True, max_length=100)),
                ('num_hijos', models.PositiveIntegerField(default=0)),
                ('embarazada', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=10)),
                ('lactante', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=10)),
                ('estado_civil', models.CharField(choices=[('SOLTERA', 'SOLTERA'), ('SOLTERO', 'SOLTERO'), ('CASADA', 'CASADA'), ('CASADO', 'CASADO'), ('DIVORCIADA', 'DIVORCIADA'), ('DIVORCIADO', 'DIVORCIADO'), ('VIUDA', 'VIUDA'), ('VIUDO', 'VIUDO'), ('CONCUBINATO', 'CONCUBINATO')], max_length=20)),
                ('educacion', models.CharField(blank=True, choices=[('ANALFABETA', 'ANALFABETA'), ('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA'), ('TECNICO MEDIO', 'TECNICO MEDIO'), ('TECNICO SUPERIOR', 'TECNICO SUPERIOR'), ('UNIVERSITARIO', 'UNIVERSITARIO')], max_length=20)),
                ('profesion', models.CharField(blank=True, max_length=25)),
                ('laboral', models.CharField(blank=True, choices=[('DESEMPLEADA', 'DESEMPLEADA'), ('DESEMPLEADO', 'DESEMPLEADO'), ('EMPLEADA', 'EMPLEADA'), ('EMPLEADO', 'EMPLEADO'), ('OCACIONAL', 'OCACIONAL'), ('INDEPENDIENTE', 'INDEPENDIENTE')], max_length=20)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('direccion', models.TextField(blank=True)),
                ('estado', models.CharField(blank=True, max_length=25)),
                ('ciudad', models.CharField(blank=True, max_length=30)),
                ('estatus', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('CERRADO', 'CERRADO'), ('EGRESO', 'EGRESO'), ('DESINCORPORACION', 'DESINCORPORACION')], default='ACTIVO', max_length=30)),
                ('numero_cuenta', models.PositiveIntegerField(blank=True, default=0)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('creado', models.DateField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
            ],
            options={
                'ordering': ('-cedula',),
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(choices=[('CONYUGUE', 'CONYUGUE'), ('SOBRINO', 'SOBRINO'), ('SOBRINA', 'SOBRINA'), ('NIETO', 'NIETO'), ('NIETA', 'NIETA'), ('ASISTIDO', 'ASISTIDO'), ('ASISTIDA', 'ASISTIDA'), ('HERMANO', 'HERMANO'), ('HERMANA', 'HERMANA'), ('TIO', 'TIO'), ('TIA', 'TIA'), ('ABUELO', 'ABUELO'), ('ABUELA', 'ABUELA')], max_length=15)),
                ('cedula', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], max_length=20)),
                ('fecha_nac', models.DateField()),
                ('edad', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('estado_civil', models.CharField(choices=[('SOLTERA', 'SOLTERA'), ('SOLTERO', 'SOLTERO'), ('CASADA', 'CASADA'), ('CASADO', 'CASADO'), ('DIVORCIADA', 'DIVORCIADA'), ('DIVORCIADO', 'DIVORCIADO'), ('VIUDA', 'VIUDA'), ('VIUDO', 'VIUDO'), ('CONCUBINATO', 'CONCUBINATO')], max_length=15)),
                ('educacion', models.CharField(blank=True, choices=[('ANALFABETA', 'ANALFABETA'), ('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA'), ('TECNICO MEDIO', 'TECNICO MEDIO'), ('TECNICO SUPERIOR', 'TECNICO SUPERIOR'), ('UNIVERSITARIO', 'UNIVERSITARIO')], max_length=20)),
                ('profesion', models.CharField(blank=True, max_length=25)),
                ('laboral', models.CharField(blank=True, choices=[('DESEMPLEADA', 'DESEMPLEADA'), ('DESEMPLEADO', 'DESEMPLEADO'), ('EMPLEADA', 'EMPLEADA'), ('EMPLEADO', 'EMPLEADO'), ('OCACIONAL', 'OCACIONAL'), ('INDEPENDIENTE', 'INDEPENDIENTE')], max_length=20)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=100, unique=True)),
                ('estatus', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('CERRADO', 'CERRADO'), ('EGRESO', 'EGRESO'), ('DESINCORPORACION', 'DESINCORPORACION')], max_length=30)),
                ('nombre_centro', models.CharField(max_length=50)),
                ('direccion', models.TextField(blank=True)),
                ('estado', models.CharField(max_length=25)),
                ('ciudad', models.CharField(max_length=30)),
                ('representante', models.CharField(blank=True, max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('estatus',),
            },
        ),
        migrations.CreateModel(
            name='Nutricional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_embarazo', models.CharField(blank=True, max_length=10)),
                ('en_lactando', models.CharField(blank=True, max_length=10)),
                ('tiempo_gestacion', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('tiempo_lactancia', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('mercado_lorealiza', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Abuelo(a)', 'Abuelo(a)'), ('Tio(a)', 'Tio(a)'), ('Otros', 'Otros')], max_length=200)),
                ('cocina_lorealiza', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Abuelo(a)', 'Abuelo(a)'), ('Tio(a)', 'Tio(a)'), ('Otros', 'Otros')], max_length=200)),
                ('frecuencia', models.CharField(blank=True, max_length=10)),
                ('apetito', models.CharField(blank=True, max_length=10)),
                ('cuantas_comidas', models.CharField(blank=True, max_length=10)),
                ('meriendas', models.CharField(blank=True, max_length=100)),
                ('cuantos_grupos', models.CharField(blank=True, max_length=10)),
                ('tipo_grupos', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cereales y Leguminosas', 'Cereales y Leguminosas'), ('Frutas y Verduras', 'Frutas y Verduras'), ('Leche, Yogures y Quesos', 'Leche, Yogures y Quesos'), ('Grasas y Aceites', 'Grasas y Aceites'), ('Dulces', 'Dulces'), ('Carnes y Huevos', 'Carnes y Huevos')], max_length=200)),
                ('cereales', models.CharField(blank=True, max_length=10)),
                ('vegetales', models.CharField(blank=True, max_length=10)),
                ('frutas', models.CharField(blank=True, max_length=10)),
                ('carnes', models.CharField(blank=True, max_length=10)),
                ('pollo', models.CharField(blank=True, max_length=10)),
                ('pescado', models.CharField(blank=True, max_length=10)),
                ('embutidos', models.CharField(blank=True, max_length=10)),
                ('viceras', models.CharField(blank=True, max_length=10)),
                ('grasas', models.CharField(blank=True, max_length=10)),
                ('lacteos', models.CharField(blank=True, max_length=10)),
                ('huevos', models.CharField(blank=True, max_length=10)),
                ('leguminosas', models.CharField(blank=True, max_length=10)),
                ('tuberculos', models.CharField(blank=True, max_length=10)),
                ('charcuteria', models.CharField(blank=True, max_length=10)),
                ('poco_vegetales', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Por Rechazo', 'Por Rechazo'), ('No sabe prepararlo', 'No sabe prepararlo'), ('Están muy costosos', 'Están muy costosos'), ('No están acostumbrados', 'No están acostumbrados')], max_length=200)),
                ('poco_frutas', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Por Rechazo', 'Por Rechazo'), ('No sabe prepararlo', 'No sabe prepararlo'), ('Están muy costosos', 'Están muy costosos'), ('No están acostumbrados', 'No están acostumbrados')], max_length=200)),
                ('poco_viceras', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Por Rechazo', 'Por Rechazo'), ('No sabe prepararlo', 'No sabe prepararlo'), ('Están muy costosos', 'Están muy costosos'), ('No están acostumbrados', 'No están acostumbrados')], max_length=200)),
                ('bonos', models.CharField(blank=True, max_length=10)),
                ('bonos_entre', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Entre 1 a 3 meses', 'Entre 1 a 3 meses'), ('Entre 3 a 6 meses', 'Entre 3 a 6 meses')], max_length=50)),
                ('clap', models.CharField(blank=True, max_length=10)),
                ('clap_entre', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Entre 1 a 3 meses', 'Entre 1 a 3 meses'), ('Entre 3 a 6 meses', 'Entre 3 a 6 meses')], max_length=50)),
                ('iglesia', models.CharField(blank=True, max_length=10)),
                ('iglesia_entre', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Entre 1 a 3 meses', 'Entre 1 a 3 meses'), ('Entre 3 a 6 meses', 'Entre 3 a 6 meses')], max_length=50)),
                ('familiar', models.CharField(blank=True, max_length=10)),
                ('familiar_entre', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Entre 1 a 3 meses', 'Entre 1 a 3 meses'), ('Entre 3 a 6 meses', 'Entre 3 a 6 meses')], max_length=50)),
                ('pensionado', models.CharField(blank=True, max_length=10)),
                ('pensionado_entre', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Entre 1 a 3 meses', 'Entre 1 a 3 meses'), ('Entre 3 a 6 meses', 'Entre 3 a 6 meses')], max_length=50)),
                ('practica_deporte', models.CharField(blank=True, max_length=10)),
                ('tiempo', models.CharField(blank=True, max_length=100)),
                ('actividad', models.CharField(blank=True, max_length=100)),
                ('medicamento', models.CharField(blank=True, max_length=10)),
                ('medicamento_suplemento', models.TextField(blank=True, max_length=150)),
                ('agua', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Tuberia sin Tratamiento', 'Tuberia sin Tratamiento'), ('Filtrada', 'Filtrada'), ('Botellon', 'Botellon'), ('Hervida', 'Hervida'), ('Tabletas Aguatab', 'Tabletas Aguatab')], max_length=200)),
                ('falla_servicio', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Agua', 'Agua'), ('Gas', 'Gas'), ('Eléctricidad', 'Eléctricidad'), ('Telefonía Internet', 'Telefonía Internet'), ('Aseo Urbano', 'Aseo Urbano')], max_length=200)),
                ('compra_gas', models.CharField(blank=True, max_length=10)),
                ('compra_agua', models.CharField(blank=True, max_length=10)),
                ('almacena_agua', models.CharField(blank=True, max_length=10)),
                ('donde_almacena', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pipote', 'Pipote'), ('Tanque', 'Tanque'), ('Otros', 'Otros')], max_length=200)),
                ('conoce_grupos', models.CharField(blank=True, max_length=50)),
                ('conoce_calidad', models.CharField(blank=True, max_length=50)),
                ('conoce_desnutricion', models.CharField(blank=True, max_length=50)),
                ('conoce_beneficio', models.CharField(blank=True, max_length=50)),
                ('embarazo', models.CharField(blank=True, max_length=100)),
                ('lactando', models.CharField(blank=True, max_length=100)),
                ('desea_amamantar', models.CharField(blank=True, max_length=100)),
                ('dificultad_amamantar', models.CharField(blank=True, max_length=100)),
                ('desea_orientacion', models.CharField(blank=True, max_length=100)),
                ('desea_conocimiento', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Menor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=15, unique=True)),
                ('parentesco', models.CharField(choices=[('HIJO', 'HIJO'), ('HIJA', 'HIJA'), ('SOBRINO', 'SOBRINO'), ('SOBRINA', 'SOBRINA'), ('NIETO', 'NIETO'), ('NIETA', 'NIETA'), ('ASISTIDO', 'ASISTIDO'), ('ASISTIDA', 'ASISTIDA')], max_length=15)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], max_length=15)),
                ('fecha_nac', models.DateField()),
                ('edad', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('fecha_ing_proyecto', models.DateField(null=True)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('estatus', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('CERRADO', 'CERRADO'), ('EGRESO', 'EGRESO'), ('DESINCORPORACION', 'DESINCORPORACION')], default=True, max_length=30)),
                ('peso_actual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('talla_actual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('imc_actual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cbi_actual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ptr_actual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('pse_actual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cc_actual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('diagnostico_actual', models.CharField(max_length=50)),
                ('diagnostico_talla_actual', models.CharField(max_length=50)),
                ('estado_nutri_actual', models.CharField(max_length=50)),
                ('creado', models.DateField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto')),
            ],
            options={
                'ordering': ('-cedula_bef',),
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Medica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('medico_tratante', models.CharField(max_length=50)),
                ('tipo_consulta', models.CharField(choices=[('JORNADA', 'JORNADA'), ('CONSULTA PROGRAMADA', 'CONSULTA PROGRAMADA'), ('EMERGENCIA', 'EMERGENCIA')], max_length=20)),
                ('examen_fisico', models.CharField(choices=[('SANO', 'SANO'), ('ANORMAL', 'ANORMAL')], max_length=10)),
                ('diagnostico1', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Niño Sano', 'Niño Sano'), ('Traumatismos varios', 'Traumatismos varios'), ('Alérgia', 'Alérgia'), ('Cefalea', 'Cefalea'), ('Hiperreactividad bronquial y rinitis', 'Hiperreactividad bronquial y rinitis')], max_length=200)),
                ('diagnostico2', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Infección respiratoria inferior', 'Infección respiratoria inferior'), ('Faringoamigdalitis', 'Faringoamigdalitis'), ('Sinusitis', 'Sinusitis'), ('Parasitosis Intestinal', 'Parasitosis Intestinal'), ('Diarreas', 'Diarreas')], max_length=200)),
                ('diagnostico3', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Dermatitis y otras afecciones de piel', 'Dermatitis y otras afecciones de piel'), ('Otitis', 'Otitis'), ('Caries dentales', 'Caries dentales'), ('Abscesos dentales', 'Abscesos dentales')], max_length=200)),
                ('otros_varios', models.TextField(blank=True, max_length=200)),
                ('desp_menor', models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('desp_familia', models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('anemico', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Suplementación de Acido Folico', 'Suplementación de Acido Folico'), ('Suplementación de Hierro', 'Suplementación de Hierro'), ('Suplementación de Minerales y Vitaminas', 'Suplementación de Minerales y Vitaminas')], max_length=200)),
                ('tratamiento', models.TextField(blank=True, max_length=200)),
                ('referencia', models.TextField(blank=True, max_length=200)),
                ('paraclinicos', models.TextField(blank=True, max_length=200)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.menor')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='jornada',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto'),
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto')),
            ],
            options={
                'ordering': ('-jornada',),
            },
        ),
        migrations.CreateModel(
            name='AntropMenor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('peso', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('talla', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cbi', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ptr', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('pse', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('cc', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('diagnostico', models.CharField(max_length=50)),
                ('diagnostico_talla', models.CharField(max_length=50)),
                ('riesgo', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=3)),
                ('servicio', models.TextField(blank=True, max_length=200)),
                ('centro_hospital', models.TextField(blank=True, max_length=200)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('min_peso', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('max_peso', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('min_talla', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('max_talla', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('min_imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('max_imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.menor')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='AntropBef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embarazo_lactando', models.CharField(blank=True, choices=[('EMBARAZADA', 'EMBARAZADA'), ('LACTANDO', 'LACTANDO')], max_length=25, null=True)),
                ('tiempo_gestacion', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('edad', models.PositiveIntegerField(default=0)),
                ('meses', models.PositiveIntegerField(default=0)),
                ('peso', models.DecimalField(decimal_places=2, help_text='Kg', max_digits=5)),
                ('talla', models.DecimalField(decimal_places=2, help_text='cm', max_digits=5)),
                ('cbi', models.DecimalField(blank=True, decimal_places=2, help_text='cm', max_digits=5, null=True)),
                ('imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('diagnostico', models.CharField(max_length=50)),
                ('riesgo', models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=3, null=True)),
                ('servicio', models.TextField(blank=True, max_length=200)),
                ('centro_hospital', models.TextField(blank=True, max_length=200)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('min_imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('max_imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
                ('jornada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.jornada')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('completado', models.DateTimeField(blank=True, null=True)),
                ('importante', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
