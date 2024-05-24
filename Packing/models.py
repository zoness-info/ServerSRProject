from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils import timezone

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

class skunamedetails(models.Model):
    category_name = models.ForeignKey(oilcategorydetails, on_delete=models.CASCADE)
    skuname = models.CharField(_("SKU Name"), max_length=50)
    skucode_m = models.CharField(_("SKU Code Master"), max_length=50, unique=True)
    skucode_c = models.CharField(_("SKU Code By Category"), max_length=50)
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
        ('Full(1)',1),
        ('Half(1/2)',0.5),
        ('QUATER(1/4)',0.25),
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
    runningmrp = models.CharField(_("Roll MRP"), max_length=50)
    runningrollno = models.CharField(_("Roll No"), max_length=50)
    runningoperatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE)
    runningpouchcount = models.IntegerField(_("Pouch Count"),blank=True, null=True)
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
        return self.maintankname
    
    
class VitaminDetails(models.Model):
    vitaminname = models.CharField(_("Vitamin Name"), max_length=50)
    units = models.IntegerField(_("Measure in Grams"))
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)
    
    def __str__(self):
        return self.vitaminname
    
class TMPSDetails(models.Model):
    units = models.IntegerField(_("Measure in ml"))
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)
    
    def __str__(self):
        return self.units
    
class TBHQDetails(models.Model):
    units = models.IntegerField(_("Measure in Grams"))
    desc = models.CharField(_("Description"), max_length=50, null=True, blank=True)
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated AT"), auto_now=True)
    isdelete = models.BooleanField(_("Deleted"),default=False)
    
    def __str__(self):
        return self.units
    
class OilPumpingDetails(models.Model):
    motorontime = models.DateTimeField(_("Motor ON Time"), auto_now=False, auto_now_add=False)  
    motorofftime = models.DateTimeField(_("Motor OFF Time"), auto_now=False, auto_now_add=False)
    shift = models.ForeignKey(DayNightshift, on_delete=models.CASCADE)
    maintank = models.ForeignKey(MainTankDetails, on_delete=models.CASCADE)
    subtank = models.ForeignKey(SubTankDetails, on_delete=models.CASCADE)
    vitaminunits = models.ForeignKey(VitaminDetails, on_delete=models.CASCADE)
    tmpsunits = models.ForeignKey(TMPSDetails, on_delete=models.CASCADE)
    tbhqunits = models.ForeignKey(TBHQDetails, on_delete=models.CASCADE)
    operatorname = models.ForeignKey(OperatorNameDetails, on_delete=models.CASCADE)
    qcname = models.ForeignKey(QCNameDetails, on_delete=models.CASCADE)
    manager = models.ForeignKey(PackingManagerDetails, on_delete=models.CASCADE)
    
    
    
    
    
    pass
# Create your models here.