#python manage.py import_excel_dispatchstock E:\datafiles\dispatchstock.xlsx


import pandas as pd
from django.core.management.base import BaseCommand
from Packing.models import DispatchOpendingClosingStockDetails


class Command(BaseCommand):
    help = 'Import data from Excel sheet'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)

        try:
            # Read Excel file into a pandas DataFrame
            df = pd.read_excel(file_path)
            df.fillna(0, inplace=True)

            # Iterate over rows in the DataFrame and create model objects
            for index, row in df.iterrows():
                try:
                    obj = DispatchOpendingClosingStockDetails(
                        date=row['DATE'],
                        skucode=row['SKU CODE'],
                        categoryname=row['BRAND NAME'],
                        skuname=row['PARTICULAR'],
                        openingstock=row['OPENING STOCK'],
                        sales=row['SALES'],
                        closingstock=row['CLOSING STOCK'],
                        production=row['PRODUCTION'],
                        noofemptycottonbox=row['no of Empty Carton Box']
                    )
                    obj.save()
                    
                except KeyError as e:
                    print(f"KeyError: {e} column not found in the Excel file.")
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))        
        except FileNotFoundError:
            print(f"File not found at {file_path}")
           

        
