from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf.global_settings import AUTH_USER_MODEL
from django.conf import settings

class branddetails(models.Model):
    brandname = models.CharField(_("Brand Name"), max_length=50)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)

    def __str__(self):
        return self.brandname

class oilcategorydetails(models.Model):
    id = models.BigAutoField(_("ID"), primary_key=True)
    brandname = models.ForeignKey(branddetails, on_delete=models.CASCADE)
    oilcategoryname = models.CharField(_("Category Name"), max_length=50, unique=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)

    def __str__(self):
        return self.oilcategoryname

class GodownDetails(models.Model):
    id = models.BigAutoField(_("ID"),primary_key=True)
    godownname = models.CharField(_("Godown Name"), max_length=50)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"), default=False)

    def __str__(self):
        return self.godownname



class skunamedetails(models.Model):
    CHOICES = {
        ('POUCH','POUCH'),
        ('PET','PET'),
        ('JAR','JAR')
    }
    category_name = models.ForeignKey(oilcategorydetails, on_delete=models.CASCADE)
    skuname = models.CharField(_("SKU Name"), max_length=50)
    skutype = models.CharField(_("SKU Type"), max_length=50,choices=CHOICES,default="POUCH")
    skucode_m = models.CharField(_("SKU Code Master"), max_length=50, unique=True)
    skucode_c = models.CharField(_("SKU Code By Category"), max_length=50)
    godownname = models.ForeignKey(GodownDetails, on_delete=models.CASCADE)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"), default=False)


    def __str__(self):
        return self.skuname

class DayNightshift(models.Model):
    choices = [
        ('Day','Day'),
        ('Night','Night'),
        ('Day-OT','Day-OT'),
        ('Night-OT','Night-OT')
    ]
    shifttype = models.CharField(_("Shift Details"), max_length=50, choices= choices)

    def __str__(self):
        return self.shifttype
class PackingManagerDetails(models.Model):
    managername = models.CharField(_("Packing Manager Name"), max_length=50)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.managername

class QCNameDetails(models.Model):
    qcname = models.CharField(_("Pouch Section Name"), max_length=50)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.qcname


class PackingSection(models.Model):
    sectionname = models.CharField(_("Pouch Section Name"), max_length=50)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.sectionname


class OperatorNameDetails(models.Model):
    empid = models.CharField(_("Employee ID"), max_length=50, primary_key=True)
    sectionname = models.ForeignKey(PackingSection, on_delete=models.CASCADE)
    operatorname = models.CharField(_("Operator Name"), max_length=50)
    mobileno = models.IntegerField(_("Mobile No"))
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.operatorname

class ChampionNameDetails(models.Model):
    contractorname = models.CharField(_("Contractor Name"), max_length=50)
    championname = models.CharField(_("Champion Name"), max_length=50, unique=True)
    wtchecker = models.CharField(_("Weight Checker Name"), max_length=50)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.championname

class PrintingRollBatch(models.Model):
    date = models.DateField()
    shift = models.ForeignKey(DayNightshift, on_delete=models.CASCADE)
    skuname = models.ForeignKey(skunamedetails, on_delete=models.CASCADE)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    batch_no = models.CharField(max_length=100)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.date} - {self.shift} - {self.skuname} - {self.mrp} - {self.batch_no} - {self.operatorname}"

class PrintingRollDetail(models.Model):
    printingrollbatch = models.ForeignKey(PrintingRollBatch, on_delete=models.CASCADE)
    filmrollno = models.CharField(_("Film Roll No"), max_length=50, primary_key=True)
    filmrolldate = models.DateField(_("Film Roll Date"), auto_now=False, auto_now_add=False)
    grosswt = models.DecimalField(_("Gross Weight"), max_digits=15, decimal_places=2)
    netwt = models.DecimalField(_("Net Weight"), max_digits=15, decimal_places=2)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)


    def __str__(self):
        return self.filmrollno



class PackingMachineDetails(models.Model):
    machineid = models.CharField(_("Machine ID"), max_length=50,primary_key=True)
    machinename = models.CharField(_("Machine Name"), max_length=50)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.machinename

class FilmRollType(models.Model):
    choices = [
        ('FULL(1)',1),
        ('HALF(1/2)',0.5),
        ('QUATOR(1/4)',0.25),
        ('THREE-FOURTH(3/4)',0.75)
    ]
    rolltype = models.CharField(_("Roll type"), max_length=50, choices= choices)

    def __str__(self):
        return self.rolltype

class ProductionRollDetails(models.Model):
    runningdate = models.DateField(auto_now=False, auto_now_add=False)
    runningshift = models.ForeignKey(DayNightshift, on_delete=models.CASCADE)
    runningmachine = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE)
    runningskuname = models.ForeignKey(skunamedetails, on_delete=models.CASCADE)
    runningrolltype = models.ForeignKey(FilmRollType, on_delete=models.CASCADE)
    runningrollstarttime = models.DateTimeField(_("Roll Start Time"), auto_now=False, auto_now_add=False)
    runningrollstoptime = models.DateTimeField(_("Roll Stop Time"), auto_now=False, auto_now_add=False)
    runningbatchno = models.CharField(_("Roll Batch No"), max_length=50)
    runningmrp = models.IntegerField(_("MRP"))
    runningrollno = models.CharField(_("Roll No"), max_length=50)
    runningoperatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE)
    runningpouchcount = models.IntegerField(_("Pouch Count"),blank=True, null=True)
    championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, null=True, blank=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)


    def __str__(self):
        return f"{self.runningdate} - {self.runningshift} - {self.runningmachine} - {self.runningskuname} - {self.runningoperatorname}"

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         # This is a new instance, so it's being created
    #         self.rollstarttime = timezone.now()
    #         self.rollstoptime = timezone.now()  # Set both start and stop time for creation
    #     else:
    #         # This is an existing instance, so it's being updated
    #         self.rollstoptime = timezone.now()  # Update stop time for every update
    #     super().save(*args, **kwargs)

class DispatchOpendingClosingStockDetails(models.Model):
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    skucode = models.CharField(_("SKUCODE"), max_length=50)
    categoryname = models.CharField(_("Category Name"), max_length=50)
    skuname = models.CharField(_("SKU Name"), max_length=50)
    openingstock = models.IntegerField(_("Opening Stock"))
    sales = models.IntegerField(_("Sales"))
    closingstock = models.IntegerField(_("Closing Stock"))
    production = models.IntegerField(_("Productin"))
    noofemptycottonbox = models.IntegerField(_("No of Empty Cotton Box"), null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str(self):
        return f'{self.date} - {self.skucode} - {self.categoryname} - {self.skuname} - {self.openingstock} - {self.sales} - {self.closingstock} - {self.production}'

class MainTankDetails(models.Model):
    maintankname = models.CharField(_("Main Tank Name"), max_length=50)
    oilname = models.CharField(_("Oil Name"), max_length=50)
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    capacity = models.IntegerField(_("Tank Capacity in MT"))
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.maintankname

class SubTankDetails(models.Model):
    subtankname = models.CharField(_("Main Tank Name"), max_length=50)
    oilname = models.CharField(_("Oil Name"), max_length=50)
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    capacity = models.IntegerField(_("Tank Capacity in MT"))
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.subtankname


class VitaminDetails(models.Model):
    vitaminname = models.CharField(_("Vitamin Name"), max_length=50)
    units = models.IntegerField(_("Measure in Grams"))
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return str(self.units)

class TMPSDetails(models.Model):
    units = models.IntegerField(_("Measure in ml"))
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return str(self.units)

class TBHQDetails(models.Model):
    units = models.IntegerField(_("Measure in Grams"))
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return str(self.units)

class OilPumpingDetails(models.Model):
    date =models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    motorontime = models.DateTimeField(_("Motor ON Time"), auto_now=False, auto_now_add=False)
    motorofftime = models.DateTimeField(_("Motor OFF Time"), auto_now=False, auto_now_add=False)
    shift = models.ForeignKey(DayNightshift, on_delete=models.CASCADE)
    maintank = models.ForeignKey(MainTankDetails, on_delete=models.CASCADE)
    subtank = models.ForeignKey(SubTankDetails, on_delete=models.CASCADE)
    vitaminunits = models.ForeignKey(VitaminDetails, on_delete=models.CASCADE, blank=True, null=True)
    tmpsunits = models.ForeignKey(TMPSDetails, on_delete=models.CASCADE)
    tbhqunits = models.ForeignKey(TBHQDetails, on_delete=models.CASCADE)
    operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE)
    qcname = models.ForeignKey(QCNameDetails, on_delete=models.CASCADE)
    manager = models.ForeignKey(PackingManagerDetails, on_delete=models.CASCADE)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return str(self.maintank)

    pass


class ChangeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=255)
    instance_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)
    changes = models.TextField()

    def __str__(self):
        return f"{self.user} {self.action} {self.model} {self.instance_id} at {self.timestamp}"


class DailyPouchCuttingDetails(models.Model):
    date = models.DateField(_("Entry Date"), auto_now=False, auto_now_add=False)
    shift = models.ForeignKey(DayNightshift, on_delete=models.CASCADE)
    operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE)
    sfleakinmt = models.DecimalField(_("SF Leak in MT"), max_digits=8, decimal_places=2)
    gnleakinmt = models.DecimalField(_("SF Leak in MT"), max_digits=8, decimal_places=2,blank=True, null=True)
    gnrleakinmt = models.DecimalField(_("SF Leak in MT"), max_digits=8, decimal_places=2,blank=True, null=True)
    rbleakinmt = models.DecimalField(_("SF Leak in MT"), max_digits=8, decimal_places=2,blank=True, null=True)
    palmleakinmt = models.DecimalField(_("SF Leak in MT"), max_digits=8, decimal_places=2,blank=True, null=True)
    ginleakinmt = models.DecimalField(_("SF Leak in MT"), max_digits=8, decimal_places=2,blank=True, null=True)
    remarks = models.CharField(_("Remarks"), max_length=50,blank=True, null=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return f'{self.date} - {self.operatorname} - {self.shift} - {self.gnleakinmt}'

class PouchLeakMistakesName(models.Model):
    mistakename = models.CharField(_("Name of Mistake"), max_length=50)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return self.mistakename

class ManualLeakChangeManpower(models.Model):
    date = models.DateField(_("Leak Change Date"), auto_now=False, auto_now_add=False)
    shift = models.ForeignKey(DayNightshift, on_delete=models.CASCADE)
    hindimanpower = models.IntegerField(_("Total Hindi Manpower"))
    ladiesmanpower = models.IntegerField(_("Total Ladies Manpower"))
    changeddamagebox = models.IntegerField(_("Total Leak Change Box"))
    remarks = models.TextField(_("Remarks"), blank=True, null=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return f'Date : {self.date} -Shift :{self.shift} Ladies : {self.ladiesmanpower} Hindi : {self.hindimanpower} - Box : {self.changeddamagebox}'



class ManualLeakChangeRollPouchFS(models.Model): #2
    manpower = models.ForeignKey(ManualLeakChangeManpower, on_delete=models.CASCADE)
    rollno = models.ForeignKey(PrintingRollDetail, on_delete=models.CASCADE)
    noofpouch = models.IntegerField(_("No of Leak Pouch"))
    mistakename = models.ForeignKey(PouchLeakMistakesName, on_delete=models.CASCADE)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return f'{self.rollno} - {self.noofpouch} - {self.mistakename}'

class ExpVsActDetails(models.Model):
    date = models.DateField(_("PPSR Date"), auto_now=False, auto_now_add=False, unique=True)
    expbox = models.IntegerField(_("Expected Box"))
    actbox = models.IntegerField(_("Actual Box"))
    remarks = models.CharField(_("Remarks"), max_length=50, null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)

    def __str__(self):
        return f'{self.date} - {self.expbox} - {self.actbox}'


class PPSRDetails(models.Model):
    OFF = 'OFF'
    ON = 'ON'
    CHOICES = [
        (OFF, _('OFF')),
        (ON, _('ON')),
    ]

    date = models.DateTimeField(_("Entry Date&Time"), auto_now=False, auto_now_add=False)
    shiftoverallplan = models.IntegerField(_("Dayshift Overall Machine Plan"))
    ipk1_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='IPK_1_machinename')
    ipk1_plan = models.IntegerField(_("IPK1 Plan"),blank=True, null=True)
    ipk1_status = models.CharField(_("IPK1 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk1_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_1_runningsku',blank=True, null=True)
    ipk1_pouchcount = models.IntegerField(_("IPK1 Pouch Count"),blank=True, null=True)
    ipk1_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_1_operatorname',blank=True, null=True)
    ipk1_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_1_championname', blank=True, null=True)
    ipk1_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_1_wtcheckername',blank=True,null=True)
    ipk1_mornstarttime = models.TimeField(_("IPK1 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk1_afnoonstarttime = models.TimeField(_("IPK1 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk2_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='ipk_2_machinename')
    ipk2_plan = models.IntegerField(_("IPK2 Plan"),blank=True, null=True)
    ipk2_status = models.CharField(_("IPK2 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk2_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_2_runningsku',blank=True, null=True)
    ipk2_pouchcount = models.IntegerField(_("IPK2 Pouch Count"),blank=True, null=True)
    ipk2_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_2_operatorname',blank=True, null=True)
    ipk2_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_2_championname', blank=True, null=True)
    ipk2_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_2_wtcheckername',blank=True,null=True)
    ipk2_mornstarttime = models.TimeField(_("IPK2 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk2_afnoonstarttime = models.TimeField(_("IPK2 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    wtmachine1_plus = models.IntegerField(_("Machine1 Plus"),blank=True, null=True)
    wtmachine1_good = models.IntegerField(_("Machine1 Good"),blank=True, null=True)
    wtmachine1_minus = models.IntegerField(_("Machine1 Minus"),blank=True, null=True)
    wtmachine1_special = models.IntegerField(_("Machine1 Special"),blank=True, null=True)
    wtmachine1_stockbox = models.IntegerField(_("Machine1 Complaint Stock Box"),blank=True, null=True)

    ipk3_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='IPK_3_machinename')
    ipk3_plan = models.IntegerField(_("IPK3 Plan"),blank=True, null=True)
    ipk3_status = models.CharField(_("IPK3 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk3_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_3_runningsku',blank=True, null=True)
    ipk3_pouchcount = models.IntegerField(_("IPK3 Pouch Count"),blank=True, null=True)
    ipk3_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_3_operatorname',blank=True, null=True)
    ipk3_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_3_championname', blank=True, null=True)
    ipk3_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_3_wtcheckername',blank=True,null=True)
    ipk3_mornstarttime = models.TimeField(_("IPK3 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk3_afnoonstarttime = models.TimeField(_("IPK3 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk4_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='ipk_4_machinename')
    ipk4_plan = models.IntegerField(_("IPK4 Plan"),blank=True, null=True)
    ipk4_status = models.CharField(_("IPK4 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF,)
    ipk4_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_4_runningsku',blank=True, null=True)
    ipk4_pouchcount = models.IntegerField(_("IPK4 Pouch Count"),blank=True, null=True)
    ipk4_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_4_operatorname',blank=True, null=True)
    ipk4_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_4_championname', blank=True, null=True)
    ipk4_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_4_wtcheckername',blank=True,null=True)
    ipk4_mornstarttime = models.TimeField(_("IPK4 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk4_afnoonstarttime = models.TimeField(_("IPK4 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    wtmachine2_plus = models.IntegerField(_("Machine2 Plus"),blank=True, null=True)
    wtmachine2_good = models.IntegerField(_("Machine2 Good"),blank=True, null=True)
    wtmachine2_minus = models.IntegerField(_("Machine2 Minus"),blank=True, null=True)
    wtmachine2_special = models.IntegerField(_("Machine2 Special"),blank=True, null=True)
    wtmachine2_stockbox = models.IntegerField(_("Machine2 Complaint Stock Box"),blank=True, null=True)

    ipk5_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='IPK_5_machinename')
    ipk5_plan = models.IntegerField(_("IPK5 Plan"),blank=True, null=True)
    ipk5_status = models.CharField(_("IPK5 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk5_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_5_runningsku',blank=True, null=True)
    ipk5_pouchcount = models.IntegerField(_("IPK5 Pouch Count"),blank=True, null=True)
    ipk5_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_5_operatorname',blank=True, null=True)
    ipk5_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_5_championname', blank=True, null=True)
    ipk5_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_5_wtcheckername',blank=True,null=True)
    ipk5_mornstarttime = models.TimeField(_("IPK5 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk5_afnoonstarttime = models.TimeField(_("IPK5 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk6_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='ipk_6_machinename')
    ipk6_plan = models.IntegerField(_("IPK6 Plan"),blank=True, null=True)
    ipk6_status = models.CharField(_("IPK6 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk6_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_6_runningsku',blank=True, null=True)
    ipk6_pouchcount = models.IntegerField(_("IPK6 Pouch Count"),blank=True, null=True)
    ipk6_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_6_operatorname',blank=True, null=True)
    ipk6_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_6_championname', blank=True, null=True)
    ipk6_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_6_wtcheckername',blank=True,null=True)
    ipk6_mornstarttime = models.TimeField(_("IPK6 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk6_afnoonstarttime = models.TimeField(_("IPK6 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    wtmachine3_plus = models.IntegerField(_("Machine3 Plus"),blank=True, null=True)
    wtmachine3_good = models.IntegerField(_("Machine3 Good"),blank=True, null=True)
    wtmachine3_minus = models.IntegerField(_("Machine3 Minus"),blank=True, null=True)
    wtmachine3_special = models.IntegerField(_("Machine3 Special"),blank=True, null=True)
    wtmachine3_stockbox = models.IntegerField(_("Machine3 Complaint Stock Box"),blank=True, null=True)

    ipk7_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='IPK_7_machinename')
    ipk7_plan = models.IntegerField(_("IPK6 Plan"),blank=True, null=True)
    ipk7_status = models.CharField(_("IPK7 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk7_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_7_runningsku',blank=True, null=True)
    ipk7_pouchcount = models.IntegerField(_("IPK7 Pouch Count"),blank=True, null=True)
    ipk7_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_7_operatorname',blank=True, null=True)
    ipk7_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_7_championname', blank=True, null=True)
    ipk7_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_7_wtcheckername',blank=True,null=True)
    ipk7_mornstarttime = models.TimeField(_("IPK7 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk7_afnoonstarttime = models.TimeField(_("IPK7 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk8_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='ipk_8_machinename')
    ipk8_plan = models.IntegerField(_("IPK8 Plan"),blank=True, null=True)
    ipk8_status = models.CharField(_("IPK8 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk8_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_8_runningsku',blank=True, null=True)
    ipk8_pouchcount = models.IntegerField(_("IPK6 Pouch Count"),blank=True, null=True)
    ipk8_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_8_operatorname',blank=True, null=True)
    ipk8_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_8_championname', blank=True, null=True)
    ipk8_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_8_wtcheckername',blank=True,null=True)
    ipk8_mornstarttime = models.TimeField(_("IPK8 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk8_afnoonstarttime = models.TimeField(_("IPK8 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    wtmachine4_plus = models.IntegerField(_("Machine4 Plus"),blank=True, null=True)
    wtmachine4_good = models.IntegerField(_("Machine4 Good"),blank=True, null=True)
    wtmachine4_minus = models.IntegerField(_("Machine4 Minus"),blank=True, null=True)
    wtmachine4_special = models.IntegerField(_("Machine4 Special"),blank=True, null=True)
    wtmachine4_stockbox = models.IntegerField(_("Machine4 Complaint Stock Box"),blank=True, null=True)

    ipk9_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='IPK_9_machinename')
    ipk9_plan = models.IntegerField(_("IPK9 Plan"),blank=True, null=True)
    ipk9_status = models.CharField(_("IPK9 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk9_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_9_runningsku',blank=True, null=True)
    ipk9_pouchcount = models.IntegerField(_("IPK9 Pouch Count"),blank=True, null=True)
    ipk9_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_9_operatorname',blank=True, null=True)
    ipk9_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_9_championname', blank=True, null=True)
    ipk9_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_9_wtcheckername',blank=True,null=True)
    ipk9_mornstarttime = models.TimeField(_("IPK9 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk9_afnoonstarttime = models.TimeField(_("IPK9 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk10_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='ipk_10_machinename')
    ipk10_plan = models.IntegerField(_("IPK10 Plan"),blank=True, null=True)
    ipk10_status = models.CharField(_("IPK10 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF)
    ipk10_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_10_runningsku',blank=True, null=True)
    ipk10_pouchcount = models.IntegerField(_("IPK10 Pouch Count"),blank=True, null=True)
    ipk10_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_10_operatorname',blank=True, null=True)
    ipk10_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_10_championname', blank=True, null=True)
    ipk10_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_10_wtcheckername',blank=True,null=True)
    ipk10_mornstarttime = models.TimeField(_("IPK10 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk10_afnoonstarttime = models.TimeField(_("IPK10 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk11_name = models.ForeignKey(PackingMachineDetails, on_delete=models.CASCADE,related_name='ipk_11_machinename',blank=True, null=True)
    ipk11_plan = models.IntegerField(_("IPK11 Plan"),blank=True, null=True)
    ipk11_status = models.CharField(_("IPK11 ON or OFF Status"), max_length=50, choices=CHOICES, default=OFF,blank=True, null=True)
    ipk11_runningsku = models.ForeignKey(skunamedetails, on_delete=models.CASCADE,related_name='ipk_11_runningsku',blank=True, null=True)
    ipk11_pouchcount = models.IntegerField(_("IPK11 Pouch Count"),blank=True, null=True)
    ipk11_operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE,related_name='ipk_11_operatorname',blank=True, null=True)
    ipk11_championname = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_11_championname', blank=True, null=True)
    ipk11_wtcheckername = models.ForeignKey(ChampionNameDetails, on_delete=models.CASCADE, related_name='ipk_11_wtcheckername',blank=True,null=True)
    ipk11_mornstarttime = models.TimeField(_("IPK11 Morning start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    ipk11_afnoonstarttime = models.TimeField(_("IPK11 Afternoon start Time"), auto_now=False, auto_now_add=False, null=True, blank=True)

    # def clean(self):
    #     super().clean()
    #     if self.ipk1_status == 'ON' and self.ipk1_runningsku:
    #         raise ValidationError({'ipk1_runningsku':'Running SKUUUUU must be select if IPK-1 ON'})

    def __str__(self):
        return f"PPSR Details {self.id} - {self.date}"

class SRDailyStockDetails(models.Model):
    CHOICES = [
        ('Morning','Morning'),
        ('Evening','Evening')
    ]
    date = models.DateTimeField(_("Date"), auto_now=False, auto_now_add=True)
    stocktype = models.CharField(_("Pouch/PET"), max_length=50,default='POUCH')
    skuname = models.ForeignKey(skunamedetails, on_delete=models.CASCADE)
    stockbox = models.IntegerField(_("Stock Box"))
    stockmode = models.CharField(_("Morning/Evening"), max_length=50,choices=CHOICES,default='Morning')
    updatedby = models.CharField(_("Updated By"), max_length=50,default='Unknown')
    godownname = models.ForeignKey(GodownDetails, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f'{self.date} - {self.stocktype} - {self.skuname} - {self.stockbox}'

class DispatchReq(models.Model):
    date = models.DateField(_("Requirement Date"), auto_now=True, auto_now_add=False)
    skuname = models.ForeignKey(skunamedetails, on_delete=models.CASCADE)
    reqbox = models.IntegerField(_("Requirement Box"))

    def __str__(self):
        return f'{self.date} - {self.skuname} - {self.reqbox}'


