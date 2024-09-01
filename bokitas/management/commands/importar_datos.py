import csv
import os
from decimal import Decimal
from django.core.management.base import BaseCommand
from bokitas.models import Diagnostico, ImcCla, ImcCla_5x, ImcEmbarazada, ImcPesoTalla_5x, ImcTalla

class Command(BaseCommand):
    help = 'Carga de datos desde un archivo csv a la base de datos'     
    def handle(self, *args, **options):
        with open('diagnostico.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                try:
                    Diagnostico.objects.create(
                        id=row[0],
                        codigo_diag=row[1],
                        diagnostico=row[2],
                        color1=row[3],
                        color2=row[4],
                        color3=row[5],
                        color4=row[6],
                        color5=row[7]
                    )
                except (ValueError, IndexError) as e:
                    print(csv_file, " Error al crear el diagnostico: ", e)

        with open('imccla.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                try:
                    ImcCla.objects.create(
                        id=row[0],
                        sexo=row[1],
                        anos=row[2],
                        meses=row[3],
                        l3sd=Decimal(row[4]),
                        l2sd=Decimal(row[5]),
                        l1sd=Decimal(row[6]),
                        sd0=Decimal(row[7]),
                        sd1=Decimal(row[8]),
                        sd2=Decimal(row[9]),
                        sd3=Decimal(row[10])
                    )
                except (ValueError, IndexError) as e:
                    print(csv_file, " Error al crear el imc: ", e)

        with open('imccla_5x.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                try:
                    ImcCla_5x.objects.create(
                        id=row[0],
                        sexo=row[1],
                        anos=row[2],
                        meses=row[3],
                        l3sd=row[4],
                        l2sd=row[5],
                        l1sd=row[6],
                        sd0=row[7],
                        sd1=row[8],
                        sd2=row[9],
                        sd3=row[10]
                    )
                except (ValueError, IndexError) as e:
                    print(csv_file, " Error al crear el imc: ", e)

        with open('imcembarazada.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                try:
                    ImcEmbarazada.objects.create(
                        id=row[0],
                        semana=row[1],
                        p2=row[2],
                        p3=row[3],
                        p4=row[4],
                        p5=row[5]
                    )
                except (ValueError, IndexError) as e:
                    print(csv_file, " Error al crear el imc: ", e)

        with open('imctalla.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                try:
                    ImcTalla.objects.create(
                        id=row[0],
                        sexo=row[1],
                        anos=row[2],
                        meses=row[3],
                        sd2_T=row[4],
                        sd1_T=row[5],
                        sd0=row[6],
                        sd1=row[7],
                        sd2=row[8]
                    )
                except (ValueError, IndexError) as e:
                    print(csv_file, " Error al crear el imc: ", e)

        with open('imcpesotalla_5x.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                try:
                    ImcPesoTalla_5x.objects.create(
                        id=row[0],
                        edad=row[1],
                        sexo=row[2],
                        talla=row[3],
                        ds3_T=row[4],
                        ds2_T=row[5],
                        ds1_T=row[6],
                        ds0=row[7],
                        ds1=row[8],
                        ds2=row[9],
                        ds3=row[10]
                    )
                except (ValueError, IndexError) as e:
                    print(csv_file, " Error al crear el imc: ", e)

        self.stdout.write(self.style.SUCCESS('Base de datos cargada con exito'))
        