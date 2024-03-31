# Generated by Django 5.0.3 on 2024-03-31 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokitas', '0002_rename_edad_meses_antropometrico_meses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntropBef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('embarazo_lactando', models.CharField(blank=True, choices=[('EMBARAZADA', 'EMBARAZADA'), ('LACTANDO', 'LACTANDO')], max_length=25, null=True)),
                ('tiempo_gestacion', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('edad', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('meses', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('peso', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('talla', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cbi', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('diagnostico', models.CharField(max_length=50)),
                ('riesgo', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=3)),
                ('servicio', models.TextField(blank=True, max_length=200)),
                ('centro_hospital', models.TextField(blank=True, max_length=200)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
            ],
        ),
        migrations.CreateModel(
            name='AntropMenor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('edad', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('meses', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('peso', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('talla', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cbi', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ptr', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('pse', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('imc', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('diagnostico', models.CharField(max_length=50)),
                ('diagnostico_talla', models.CharField(max_length=50)),
                ('riesgo', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=3)),
                ('servicio', models.TextField(blank=True, max_length=200)),
                ('centro_hospital', models.TextField(blank=True, max_length=200)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.familia')),
                ('cedula_bef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bokitas.beneficiario')),
            ],
        ),
        migrations.DeleteModel(
            name='Antropometrico',
        ),
    ]
