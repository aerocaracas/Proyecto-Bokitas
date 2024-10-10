# Generated by Django 5.0.3 on 2024-10-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokitas', '0003_vacunas_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacunas',
            name='dosis',
            field=models.CharField(choices=[('1ra DOSIS', '1ra DOSIS'), ('2da DOSIS', '2da DOSIS'), ('3ra DOSIS', '3ra DOSIS'), ('4ta DOSIS', '4ta DOSIS'), ('5ta DOSIS', '5ta DOSIS'), ('REFUERZO 1ra DOSIS', 'REFUERZO 1ra DOSIS'), ('REFUERZO 2da DOSIS', 'REFUERZO 2da DOSIS'), ('REFUERZO 3ra DOSIS', 'REFUERZO 3ra DOSIS')], max_length=50),
        ),
    ]
