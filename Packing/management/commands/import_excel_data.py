# myapp/management/commands/import_excel_data.py
# Run below comment to write db from excel
#python manage.py import_excel_data /path/to/your/excel/file.xlsx

#python manage.py importexceldata /path/to/your/excel/file.xlsx SheetName
#python manage.py import_excel_data E:\datafiles\masterdata.xlsx


#file_path = "E:\datafiles\masterdata.xlsx"

import os
import openpyxl
from django.core.management.base import BaseCommand
from Packing.models import (
                    branddetails, oilcategorydetails, skunamedetails, 
                            PrintingRollBatch,PrintingRollDetail, DayNightshift, 
                            FilmRollType, OperatorNameDetails, PackingMachineDetails, 
                            ProductionRollDetails, PackingSection
)

class Command(BaseCommand):
    help = 'Import data from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File '{file_path}' does not exist"))
            return

        try:
            wb = openpyxl.load_workbook(file_path)

            # Process each sheet for the corresponding model
            self.import_brand_details(wb['brandname'])
            self.import_day_night_shift(wb['shift'])
            self.import_packing_section(wb['packingsection'])
            self.import_operator_name_details(wb['operatorname'])
            self.import_oil_category_details(wb['oilcategory'])
            self.import_sku_name_details(wb['sku'])
            self.import_packing_machine_details(wb['packmachine'])
            

            self.stdout.write(self.style.SUCCESS('All Data imported successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))

    def import_brand_details(self, sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            branddetails.objects.create(brandname=row[0])  # Adjust fields accordingly
        self.stdout.write(self.style.SUCCESS('Brand Name imported successfully'))

    def import_day_night_shift(self, sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            DayNightshift.objects.create(shifttype=row[0])  # Adjust fields accordingly
        self.stdout.write(self.style.SUCCESS('Shift Details imported successfully'))
        
    def import_packing_section(self, sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            PackingSection.objects.create(sectionname=row[0])  # Adjust fields accordingly
        self.stdout.write(self.style.SUCCESS('Packing Section imported successfully'))    
        
        
    def import_operator_name_details(self, sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            sectionname_str = row[1]
            sectionname, createdat = PackingSection.objects.get_or_create(sectionname=sectionname_str)
            OperatorNameDetails.objects.create(empid=row[0],sectionname=sectionname,operatorname=row[2],mobileno=row[3])  # Adjust fields accordingly
        self.stdout.write(self.style.SUCCESS('Operator Details imported successfully'))
    
    def import_oil_category_details(self, sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            brandname_str = row[0]
            brandname, createdat = branddetails.objects.get_or_create(brandname=brandname_str)
            oilcategorydetails.objects.create(brandname=brandname,oilcategoryname=row[1])  # Adjust fields accordingly
        self.stdout.write(self.style.SUCCESS('Oil Category Details imported successfully'))
        
    def import_sku_name_details(self, sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            category_id_str = row[0]
            # print(category_id_str)
            try:
                category, created = oilcategorydetails.objects.get_or_create(oilcategoryname=category_id_str)
                # print(category.id,category.brandname,category.oilcategoryname)
                
                skunamedetails.objects.create(category_name=category,skuname=row[1],skucode_m=row[2],skucode_c=row[3])  # Adjust fields accordingly
            except oilcategorydetails.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"OilCategoryDetails with id {category_id_str} does not exist"))        
        self.stdout.write(self.style.SUCCESS('SKU Details imported successfully'))
        
    def import_packing_machine_details(self, sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            PackingMachineDetails.objects.create(machineid=row[0],machinename=row[1])  # Adjust fields accordingly
        self.stdout.write(self.style.SUCCESS('Packing Machine Details imported successfully'))