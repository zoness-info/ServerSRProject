from django.contrib import admin

from .models import CustomUser
from Packing.models import (branddetails, oilcategorydetails, skunamedetails, 
                            PrintingRollBatch,PrintingRollDetail, DayNightshift, 
                            FilmRollType, OperatorNameDetails, PackingMachineDetails, 
                            ProductionRollDetails, PackingSection,
                            MainTankDetails, SubTankDetails,VitaminDetails,TMPSDetails,TBHQDetails,OilPumpingDetails,QCNameDetails,
                            PackingManagerDetails,
                            ChangeLog,
                            DailyPouchCuttingDetails,
                            PouchLeakMistakesName,
                             ManualLeakChangeManpower, ManualLeakChangeRollPouchFS,
                             ExpVsActDetails,
                             DispatchOpendingClosingStockDetails,
                             PPSRDetails,ChampionNameDetails,
                             
                            )



class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]
admin.site.register(CustomUser, CustomUserAdmin)




class BrandDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in branddetails._meta.fields]
        
    def save_model(self, request, obj, form, change):
        if change:  # If this is an update
            print(f'Updating: {obj}')
            obj.save()
        else:  # If this is a new record
            print(f'Creating new record: {obj}')
            obj.save()
admin.site.register(branddetails, BrandDetailsAdmin)    

class OilCategoryDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in oilcategorydetails._meta.fields]
admin.site.register(oilcategorydetails, OilCategoryDetailsAdmin)    

class SkuNameDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in skunamedetails._meta.fields]
admin.site.register(skunamedetails, SkuNameDetailsAdmin)

class PrintingRollBatchsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PrintingRollBatch._meta.fields]
admin.site.register(PrintingRollBatch, PrintingRollBatchsAdmin)

class PrintingRollDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PrintingRollDetail._meta.fields]
admin.site.register(PrintingRollDetail,PrintingRollDetailAdmin)

class DayNightshiftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DayNightshift._meta.fields]
admin.site.register(DayNightshift,DayNightshiftAdmin)

class FilmRollTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FilmRollType._meta.fields]
admin.site.register(FilmRollType,FilmRollTypeAdmin)

class OperatorNameDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OperatorNameDetails._meta.fields]
admin.site.register(OperatorNameDetails,OperatorNameDetailsAdmin)


class PackingMachineDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PackingMachineDetails._meta.fields]
admin.site.register(PackingMachineDetails,PackingMachineDetailsAdmin)

class ProductionRollDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductionRollDetails._meta.fields]
admin.site.register(ProductionRollDetails,ProductionRollDetailsAdmin)

class PackingSectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PackingSection._meta.fields]
admin.site.register(PackingSection,PackingSectionAdmin)

class MainTankDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MainTankDetails._meta.fields]
admin.site.register(MainTankDetails,MainTankDetailsAdmin)

class SubTankDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SubTankDetails._meta.fields]
admin.site.register(SubTankDetails,SubTankDetailsAdmin)

class VitaminDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VitaminDetails._meta.fields]
admin.site.register(VitaminDetails,VitaminDetailsAdmin)

class TMPSDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TMPSDetails._meta.fields]
admin.site.register(TMPSDetails,TMPSDetailsAdmin)

class TBHQDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TBHQDetails._meta.fields]
admin.site.register(TBHQDetails,TBHQDetailsAdmin)

class OilPumpingDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OilPumpingDetails._meta.fields]
admin.site.register(OilPumpingDetails,OilPumpingDetailsAdmin)

class QCNameDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QCNameDetails._meta.fields]
admin.site.register(QCNameDetails,QCNameDetailsAdmin)

class PackingManagerDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PackingManagerDetails._meta.fields]
admin.site.register(PackingManagerDetails,PackingManagerDetailsAdmin)

class ChangeLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ChangeLog._meta.fields]
admin.site.register(ChangeLog,ChangeLogAdmin)

class DailyPouchCuttingDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DailyPouchCuttingDetails._meta.fields]
admin.site.register(DailyPouchCuttingDetails,DailyPouchCuttingDetailsAdmin)

class PouchLeakMistakesNameAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PouchLeakMistakesName._meta.fields]
admin.site.register(PouchLeakMistakesName,PouchLeakMistakesNameAdmin)#-------

class ManualLeakChangeManpowerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ManualLeakChangeManpower._meta.fields]
admin.site.register(ManualLeakChangeManpower,ManualLeakChangeManpowerAdmin)

class ManualLeakChangeRollPouchFSAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ManualLeakChangeRollPouchFS._meta.fields]
admin.site.register(ManualLeakChangeRollPouchFS,ManualLeakChangeRollPouchFSAdmin)

class ExpVsActDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExpVsActDetails._meta.fields]
admin.site.register(ExpVsActDetails,ExpVsActDetailsAdmin)

class DispatchOpendingClosingStockDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DispatchOpendingClosingStockDetails._meta.fields]
admin.site.register(DispatchOpendingClosingStockDetails,DispatchOpendingClosingStockDetailsAdmin)

class PPSRDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PPSRDetails._meta.fields]
admin.site.register(PPSRDetails,PPSRDetailsAdmin)

class ChampionNameDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ChampionNameDetails._meta.fields]
admin.site.register(ChampionNameDetails,ChampionNameDetailsAdmin)

# Register your models here.
