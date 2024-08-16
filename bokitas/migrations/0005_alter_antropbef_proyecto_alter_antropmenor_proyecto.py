# Generated by Django 5.0.3 on 2024-08-16 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokitas', '0004_antropbef_proyecto_alter_menor_parentesco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antropbef',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto'),
        ),
        migrations.AlterField(
            model_name='antropmenor',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.proyecto'),
        ),
    ]
