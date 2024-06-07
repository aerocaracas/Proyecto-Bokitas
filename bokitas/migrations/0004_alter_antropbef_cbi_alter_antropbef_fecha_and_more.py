# Generated by Django 5.0.3 on 2024-06-01 12:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokitas', '0003_antropbef_antropmenor_delete_antropometrico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antropbef',
            name='cbi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='antropbef',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='antropbef',
            name='riesgo',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='antropmenor',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='educacion',
            field=models.CharField(blank=True, choices=[('ANALFABETA', 'ANALFABETA'), ('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA'), ('TECNICO MEDIO', 'TECNICO MEDIO'), ('TECNICO SUPERIOR', 'TECNICO SUPERIOR'), ('UNIVERSITARIO', 'UNIVERSITARIO')], max_length=20),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='estado_civil',
            field=models.CharField(choices=[('SOLTERA', 'SOLTERA'), ('CASADA', 'CASADA'), ('DIVORCIADA', 'DIVORCIADA'), ('VIUDA', 'VIUDA'), ('CONCUBINATO', 'CONCUBINATO')], max_length=20),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='laboral',
            field=models.CharField(blank=True, choices=[('DESEMPLEADA', 'DESEMPLEADA'), ('EMPLEADA', 'EMPLEADA'), ('OCACIONAL', 'OCACIONAL'), ('INDEPENDIENTE', 'INDEPENDIENTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='familia',
            name='educacion',
            field=models.CharField(choices=[('ANALFABETA', 'ANALFABETA'), ('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA'), ('TECNICO MEDIO', 'TECNICO MEDIO'), ('TECNICO SUPERIOR', 'TECNICO SUPERIOR'), ('UNIVERSITARIO', 'UNIVERSITARIO')], max_length=20),
        ),
        migrations.AlterField(
            model_name='familia',
            name='estado_civil',
            field=models.CharField(choices=[('SOLTERA', 'SOLTERA'), ('CASADA', 'CASADA'), ('DIVORCIADA', 'DIVORCIADA'), ('VIUDA', 'VIUDA'), ('CONCUBINATO', 'CONCUBINATO')], max_length=15),
        ),
        migrations.AlterField(
            model_name='familia',
            name='laboral',
            field=models.CharField(blank=True, choices=[('DESEMPLEADA', 'DESEMPLEADA'), ('EMPLEADA', 'EMPLEADA'), ('OCACIONAL', 'OCACIONAL'), ('INDEPENDIENTE', 'INDEPENDIENTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='familia',
            name='parentesco',
            field=models.CharField(choices=[('CONYUGUE', 'CONYUGUE'), ('SOBRINO', 'SOBRINO'), ('NIETO', 'NIETO'), ('ASISTIDO', 'ASISTIDO'), ('HERMANO', 'HERMANO'), ('TIA', 'TIA'), ('ABUELA', 'ABUELA')], max_length=15),
        ),
    ]