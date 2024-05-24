from django.forms import ModelForm
from django import forms
from .models import branddetails, PrintingRollBatch, PrintingRollDetail, ProductionRollDetails
from django.forms import inlineformset_factory
#from django_select2.forms import Select2Widget

class branddetailsform(ModelForm):
    model = branddetails
    fields = '__all__'
    
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
            'runningrollstarttime' : forms.DateTimeInput(attrs={'class': 'form-control datepicker-time',}),
            'runningrollstoptime'  :forms.TextInput(attrs={'class': 'form-control datepicker-time',}),
            'runningbatchno'    :  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Batch No'}),
            'runningmrp'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MRP'}),
            'runningrollno'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Film Roll No'}),
            'runningoperatorname'  : forms.Select(attrs={'class': 'form-select', 'placeholder' : 'Operator Name'}),
            'runningpouchcount' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pouch Count'}),
        }
        
        
        # filmrolldate = forms.DateTimeField(label=_("Film Roll Date and Time"),widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),)