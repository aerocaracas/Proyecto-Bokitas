# Generated by Django 5.0.3 on 2024-11-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokitas', '0013_alter_nutricional_jornada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutricional',
            name='bonos_entre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='nutricional',
            name='clap_entre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='nutricional',
            name='familiar_entre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='nutricional',
            name='iglesia_entre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='nutricional',
            name='pensionado_entre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
