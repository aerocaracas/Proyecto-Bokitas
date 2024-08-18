# Generated by Django 5.0.3 on 2024-08-18 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokitas', '0009_alter_jornada_options_rename_fecha_jornada_jornada_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudades',
            old_name='Ciudad',
            new_name='ciudad',
        ),
        migrations.AlterField(
            model_name='ciudades',
            name='d_estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bokitas.estados'),
        ),
    ]
