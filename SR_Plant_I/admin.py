from django.contrib import admin

from .models import CustomUser
from Packing.models import (branddetails, oilcategorydetails, skunamedetails, 
                            PrintingRollBatch,PrintingRollDetail, DayNightshift, 
                            FilmRollType, OperatorNameDetails, PackingMachineDetails, 
                            ProductionRollDetails, PackingSection)


admin.site.register(CustomUser)


class BrandDetailsAdmin(admin.ModelAdmin):
    list_display = ('brandname', 'createdat', 'updatedat')
    
    def save_model(self, request, obj, form, change):
        if change:  # If this is an update
            print(f'Updating: {obj}')
            obj.save()
        else:  # If this is a new record
            print(f'Creating new record: {obj}')
            obj.save()
    

class OilCategoryDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','brandname', 'oilcategoryname',  'createdat', 'updatedat')
    

class SkuNameDetailsAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'skuname',  'skucode_m', 'skucode_c','isdelete','createdat', 'updatedat')
    

admin.site.register(branddetails, BrandDetailsAdmin)
admin.site.register(oilcategorydetails, OilCategoryDetailsAdmin)
admin.site.register(skunamedetails, SkuNameDetailsAdmin)

admin.site.register(PrintingRollBatch)
admin.site.register(PrintingRollDetail)
admin.site.register(DayNightshift)

admin.site.register(FilmRollType)
admin.site.register(OperatorNameDetails)
admin.site.register(PackingMachineDetails)
admin.site.register(ProductionRollDetails)
admin.site.register(PackingSection)


# Register your models here.
