# Generated by Django 5.0.3 on 2024-08-29 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bokitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antropbef',
            old_name='fecha',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='antropmenor',
            old_name='fecha',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='medica',
            old_name='fecha',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='medicamento',
            old_name='fecha',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='nutricional',
            old_name='fecha',
            new_name='creado',
        ),
    ]
