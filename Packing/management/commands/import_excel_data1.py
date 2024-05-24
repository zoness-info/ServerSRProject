# myapp/management/commands/import_excel_data.py
# Run below comment to write db from excel
#python manage.py import_excel_data /path/to/your/excel/file.xlsx

#python manage.py importexceldata /path/to/your/excel/file.xlsx SheetName
#python manage.py import_excel_data E:\datafiles\masterdata.xlsx brandname


#file_path = "E:\datafiles\masterdata.xlsx"

import os
import openpyxl
from django.core.management.base import BaseCommand
from Packing.models import branddetails, DayNightshift

class Command(BaseCommand):
    help = 'Import data from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to Excel file')
        parser.add_argument('sheet_name', type=str, help='Name of the Excel sheet')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        sheet_name = kwargs['sheet_name']
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File '{file_path}' does not exist"))
            return

        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb[sheet_name]
            
            for row in sheet.iter_rows(min_row=2, values_only=True):
                # Process each row starting from the second row
                # For example:
                branddetails.objects.create(brandname=row[0])
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            print("exp error")
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))