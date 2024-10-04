import pandas as pd
from django.core.management.base import BaseCommand
from api.models import Make, Model, CarType


class Command(BaseCommand):
    help = 'Import car data from Excel file'

    def handle(self, *args, **kwargs):
        df = pd.read_excel('path/to/cars.xlsx')

        for _, row in df.iterrows():
            make, created = Make.objects.get_or_create(name=row['Make'])
            model, created = Model.objects.get_or_create(name=row['Model'], make=make)
            car_type, created = CarType.objects.get_or_create(name=row['Type'], model=model)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
