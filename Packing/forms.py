from django.forms import ModelForm, modelformset_factory
from django import forms
from django.core.exceptions import ValidationError
from .models import (branddetails, skunamedetails,
                     PrintingRollBatch, 
                     PrintingRollDetail, 
                     ProductionRollDetails,
                     OilPumpingDetails,
                     DailyPouchCuttingDetails,
                     ManualLeakChangeManpower,ManualLeakChangeRollPouchFS,
                     ExpVsActDetails,
                     PPSRDetails,
                     SRDailyStockDetails,
                     )
from django.forms import inlineformset_factory
#from django_select2.forms import Select2Widget

class branddetailsform(ModelForm):
    model = branddetails
    fields = '__all__'
class skunamedetailsForm(ModelForm):
    class Meta:
        model = skunamedetails
        fields = ['skuname']
    
class prinitingrolldetailsform(ModelForm):
    class Meta:
        model = PrintingRollBatch
        fields = '__all__'
        
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control datepicker', 'type':'date'}),
            # 'shift': Select2Widget(attrs={'class': 'form-select'}),
            # 'skuname': Select2Widget(attrs={'class': 'form-select'}),
            'shift': forms.Select(attrs={'class': 'form-select'}),
            'skuname': forms.Select(attrs={'class': 'form-select'}),
            'mrp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MRP'}),
            'batch_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch No'}),
            'operatorname': forms.Select(attrs={'class': 'form-select'}),
        }

class PrintingRollDetailForm(forms.ModelForm):
    class Meta:
        model = PrintingRollDetail
        fields = ['filmrollno', 'filmrolldate', 'grosswt', 'netwt']
        
        widgets = {
            'filmrollno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Film Roll No'}),
            'filmrolldate': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'grosswt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Gross Weight'}),
            'netwt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Net Weight'}),
        }
RollDetailsFormset = inlineformset_factory(PrintingRollBatch,PrintingRollDetail,form=PrintingRollDetailForm, extra=10,can_delete=True)
    
class ProductionRollDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductionRollDetails
        fields = ['runningdate','runningshift','runningmachine','runningskuname','runningrolltype','runningrollstarttime','runningrollstoptime','runningbatchno','runningmrp','runningrollno','runningoperatorname','runningpouchcount']
        
        widgets = {
            'runningdate'       : forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'runningshift'      : forms.Select(attrs={'class': 'form-select'}),
            'runningmachine'    : forms.Select(attrs={'class': 'form-select'}),
            'runningskuname'    : forms.Select(attrs={'class': 'form-select'}),
            'runningrolltype'   : forms.Select(attrs={'class': 'form-select'}), 
            'runningrollstarttime' : forms.DateTimeInput(attrs={'class': 'form-control datepicker-time','type': 'datetime-local'}),
            'runningrollstoptime'  :forms.DateTimeInput(attrs={'class': 'form-control datepicker-time','type': 'datetime-local'}),
            'runningbatchno'    :  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Batch No'}),
            'runningmrp'        : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MRP'}),
            'runningrollno'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Film Roll No'}),
            'runningoperatorname'  : forms.Select(attrs={'class': 'form-select', 'placeholder' : 'Operator Name'}),
            'runningpouchcount' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pouch Count'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProductionRollDetailsForm, self).__init__(*args, **kwargs)
        self.fields['runningrollstarttime'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['runningrollstoptime'].widget.attrs.update({'class': 'form-control datepicker'})
    
        # filmrolldate = forms.DateTimeField(label=_("Film Roll Date and Time"),widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),)



class OilPumpingDetailsForm(forms.ModelForm):
    class Meta:
        model = OilPumpingDetails
        fields = '__all__'
        widgets = {
            'date' : forms.DateInput(attrs={'class': 'form-control','type': 'date'},),
            'motorontime': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'},),
            'motorofftime': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'}),
        }
       
    def __init__(self, *args, **kwargs):
        super(OilPumpingDetailsForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control','type':'date'})
        self.fields['motorontime'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['motorofftime'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['shift'].widget.attrs.update({'class': 'form-select'})
        self.fields['maintank'].widget.attrs.update({'class': 'form-select'})
        self.fields['vitaminunits'].widget.attrs.update({'class': 'form-select'})
        self.fields['tmpsunits'].widget.attrs.update({'class': 'form-select'})
        self.fields['operatorname'].widget.attrs.update({'class': 'form-select'})
        self.fields['tbhqunits'].widget.attrs.update({'class': 'form-select'})
        self.fields['qcname'].widget.attrs.update({'class': 'form-select'})
        self.fields['subtank'].widget.attrs.update({'class': 'form-select'})
        
        self.fields['manager'].widget.attrs.update({'class': 'form-select',})

class DailyPouchCuttingDetailsForm(forms.ModelForm):
    class Meta:
        model = DailyPouchCuttingDetails
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'},),
            'remarks' : forms.Textarea(attrs={'class' : 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super(DailyPouchCuttingDetailsForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control','type':'date'})
        self.fields['shift'].widget.attrs.update({'class': 'form-select'})
        self.fields['operatorname'].widget.attrs.update({'class': 'form-select'})
        self.fields['sfleakinmt'].widget.attrs.update({'class': 'form-control','type':'text'})
        self.fields['gnleakinmt'].widget.attrs.update({'class': 'form-control','type':'text'})
        self.fields['gnrleakinmt'].widget.attrs.update({'class': 'form-control','type':'text'})
        self.fields['rbleakinmt'].widget.attrs.update({'class': 'form-control','type':'text'})
        self.fields['palmleakinmt'].widget.attrs.update({'class': 'form-control','type':'text'})
        self.fields['ginleakinmt'].widget.attrs.update({'class': 'form-control','type':'text'})
        
        self.fields['remarks'].widget.attrs.update({'class': 'form-control',})

class ManualLeakChangeManpowerForm(forms.ModelForm):
    class Meta:
        model = ManualLeakChangeManpower
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control','type': 'date'},),
            'remarks' : forms.Textarea(attrs={'class' : 'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super(ManualLeakChangeManpowerForm, self).__init__(*args, **kwargs)
        self.fields['shift'].widget.attrs.update({'class': 'form-select'})
        self.fields['date'].widget.attrs.update({'class': 'form-control','type':'date'})
        self.fields['hindimanpower'].widget.attrs.update({'class': 'form-control','type':'number'})
        self.fields['ladiesmanpower'].widget.attrs.update({'class': 'form-control','type':'number'})
        self.fields['changeddamagebox'].widget.attrs.update({'class': 'form-control','type':'number'})
        self.fields['remarks'].widget.attrs.update({'class': 'form-control','type':'text'})
        
        
       
        
class ManualLeakChangeRollPouchFSForm(forms.ModelForm):
    class Meta:
        model = ManualLeakChangeRollPouchFS
        fields = "__all__"
        
        widgets = {
            'rollno': forms.NumberInput(attrs={'class': 'form-control'}),
            'noofpouch' : forms.NumberInput(attrs={'class' : 'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ManualLeakChangeRollPouchFSForm, self).__init__(*args, **kwargs)
        self.fields['rollno'].widget.attrs.update({'class': 'form-control','type':'number'})
        self.fields['noofpouch'].widget.attrs.update({'class': 'form-control','type':'number'})
        self.fields['mistakename'].widget.attrs.update({'class': 'form-select'})

class ExpVsActDetailsForm(ModelForm):
    class Meta:
        model = ExpVsActDetails
        fields = "__all__"
        
        widgets = {
            'date'   : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'expbox' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'act' : forms.NumberInput(attrs={'class' : 'form-control'})            
        }
    def __init__(self, *args, **kwargs):
        super(ExpVsActDetailsForm,self).__init__(*args,**kwargs)
        self.fields['date'].widget.attrs.update({'class':'form-control', 'type':'date'})
        self.fields['expbox'].widget.attrs.update({'class':'form-control', 'type':'number'})
        self.fields['actbox'].widget.attrs.update({'class':'form-control', 'type':'number'})
        self.fields['remarks'].widget.attrs.update({'class':'form-control', 'type':'text'})

class DispatchStockUploadForm(forms.Form):
    file = forms.FileField(label='Select Excel File', required=True)
    
class PPSRDetailsForm(forms.ModelForm):
    class Meta:
        model = PPSRDetails
        fields = '__all__'
        
        widgets = {
            'shiftoverallplan' : forms.NumberInput(attrs=({'class':'form-control'})),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'ipk1_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk1_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk1_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk1_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk1_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk1_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk1_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk1_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk1_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk1_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk2_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk2_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk2_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk2_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk2_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk2_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk2_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk2_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk2_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk2_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'wtmachine1_plus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine1_good' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine1_minus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine1_special' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine1_stockbox' : forms.NumberInput(attrs={'class':'form-control'}),
            
            'ipk3_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk3_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk3_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk3_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk3_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk3_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk3_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk3_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk3_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk3_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk4_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk4_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk4_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk4_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk4_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk4_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk4_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk4_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk4_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk4_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'wtmachine2_plus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine2_good' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine2_minus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine2_special' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine2_stockbox' : forms.NumberInput(attrs={'class':'form-control'}),
                        
    
            'ipk5_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk5_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk5_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk5_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk5_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk5_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk5_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk5_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk5_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk5_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk6_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk6_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk6_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk6_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk6_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk6_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk6_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk6_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk6_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk6_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'wtmachine3_plus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine3_good' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine3_minus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine3_special' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine3_stockbox' : forms.NumberInput(attrs={'class':'form-control'}),
            
            'ipk7_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk7_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk7_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk7_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk7_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk7_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk7_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk7_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk7_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk7_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk8_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk8_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk8_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk8_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk8_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk8_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk8_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk8_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk8_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk8_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'wtmachine4_plus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine4_good' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine4_minus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine4_special' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine4_stockbox' : forms.NumberInput(attrs={'class':'form-control'}),
           
            'ipk9_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk9_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk9_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk9_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk9_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk9_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk9_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk9_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk9_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk9_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk10_name'     : forms.Select(attrs={'class': 'form-select'}),
            'ipk10_plan'     : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk10_status'   : forms.Select(attrs={'class':'form-select'}),
            'ipk10_runningsku': forms.Select(attrs={'class':'form-select'}),
            'ipk10_pouchcount' : forms.NumberInput(attrs={'class':'form-control'}),
            'ipk10_operatorname' : forms.Select(attrs={'class':'form-select'}),
            'ipk10_championname' : forms.Select(attrs={'class':'form-select'}),
            'ipk10_wtcheckername' : forms.Select(attrs={'class':'form-select'}),
            'ipk10_mornstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'ipk10_afnoonstarttime' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'wtmachine5_plus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine5_good' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine5_minus' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine5_special' : forms.NumberInput(attrs={'class':'form-control'}),
            'wtmachine5_stockbox' : forms.NumberInput(attrs={'class':'form-control'}),
              
            
           
            
            
            }
        
    def __init__(self, *args, **kwargs):
        super(PPSRDetailsForm,self).__init__(*args,**kwargs)
        self.fields['date'].widget.attrs.update({'class':'form-control', 'type':'date'})
        self.fields['ipk1_status'].widget.attrs.update({'class':'form-select'})  
        
        
    def clean(self):
        cleaned_data = super().clean()
        ipk1_status = cleaned_data.get('ipk1_status')
        ipk1_runningsku = cleaned_data.get('ipk1_runningsku')
        ipk2_status = cleaned_data.get('ipk2_status')
        ipk2_runningsku = cleaned_data.get('ipk2_runningsku')
        ipk3_status = cleaned_data.get('ipk3_status')
        ipk3_runningsku = cleaned_data.get('ipk3_runningsku')
        ipk4_status = cleaned_data.get('ipk4_status')
        ipk4_runningsku = cleaned_data.get('ipk4_runningsku')
        ipk5_status = cleaned_data.get('ipk5_status')
        ipk5_runningsku = cleaned_data.get('ipk5_runningsku')
        ipk6_status = cleaned_data.get('ipk6_status')
        ipk6_runningsku = cleaned_data.get('ipk6_runningsku')
        ipk7_status = cleaned_data.get('ipk7_status')
        ipk7_runningsku = cleaned_data.get('ipk7_runningsku')
        ipk8_status = cleaned_data.get('ipk8_status')
        ipk8_runningsku = cleaned_data.get('ipk8_runningsku')
        ipk9_status = cleaned_data.get('ipk9_status')
        ipk9_runningsku = cleaned_data.get('ipk9_runningsku')
        ipk10_status = cleaned_data.get('ipk10_status')
        ipk10_runningsku = cleaned_data.get('ipk10_runningsku')
        
        if ipk1_status == 'ON' and not ipk1_runningsku:
            self.add_error('ipk1_runningsku', "Running SKU must be selected if IPK1 is ON.")
        if ipk2_status == 'ON' and not ipk2_runningsku:
            self.add_error('ipk2_runningsku', "Running SKU must be selected if IPK2 is ON.")
        if ipk3_status == 'ON' and not ipk3_runningsku:
            self.add_error('ipk3_runningsku', "Running SKU must be selected if IPK3 is ON.")
        if ipk4_status == 'ON' and not ipk4_runningsku:
            self.add_error('ipk4_runningsku', "Running SKU must be selected if IPK4 is ON.")
        if ipk5_status == 'ON' and not ipk5_runningsku:
            self.add_error('ipk5_runningsku', "Running SKU must be selected if IPK5 is ON.")
        if ipk6_status == 'ON' and not ipk6_runningsku:
            self.add_error('ipk6_runningsku', "Running SKU must be selected if IPK6 is ON.")
        if ipk7_status == 'ON' and not ipk7_runningsku:
            self.add_error('ipk7_runningsku', "Running SKU must be selected if IPK7 is ON.")
        if ipk8_status == 'ON' and not ipk8_runningsku:
            self.add_error('ipk8_runningsku', "Running SKU must be selected if IPK8 is ON.")
        if ipk9_status == 'ON' and not ipk9_runningsku:
            self.add_error('ipk9_runningsku', "Running SKU must be selected if IPK9 is ON.")
        if ipk10_status == 'ON' and not ipk10_runningsku:
            self.add_error('ipk10_runningsku', "Running SKU must be selected if IPK10 is ON.")
    
        return cleaned_data
class SRDailyStockDetailsForm(forms.Form):
    def __init__(self, skuname, *args, **kwargs):
        super(SRDailyStockDetailsForm,self).__init__(*args,**kwargs)
        for sku in skuname:
            self.fields[sku.skuname] = forms.IntegerField(label=sku.skuname,required=True)
# class UniqueOverallProductionPlanFormSet(forms.BaseModelFormSet):
#     def clean(self):
#         if any(self.errors):
#             return
#         return self.cleaned_data  # Return the cleaned data after validation

#         # overallproductionplan_set = set()
#         # for form in self.forms:
#         #     if self.can_delete and self._should_delete_form(form):
#         #         continue
#         #     overallproductionplan = form.cleaned_data.get('overallproductionplan')
#         #     if overallproductionplan:
#         #         if overallproductionplan in overallproductionplan_set:
#         #             raise ValidationError("The overall production plan must be unique.")
#         #         overallproductionplan_set.add(overallproductionplan)
        
# PPSRDetailsFormSet = modelformset_factory(
#     PPSRDetails,
#     form=PPSRDetailsForm,
#     formset=UniqueOverallProductionPlanFormSet,
#     extra=1
# )