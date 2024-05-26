from django.shortcuts import get_object_or_404, redirect, render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.forms import inlineformset_factory
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta, datetime, date
import logging
from .models import (branddetails, oilcategorydetails, skunamedetails, 
                     PrintingRollBatch, PrintingRollDetail, 
                     ProductionRollDetails,
                     OilPumpingDetails, 
                     ChangeLog,
                     DailyPouchCuttingDetails,
                     ManualLeakChangeManpower,ManualLeakChangeRollPouchFS
                     )
from .forms import (branddetailsform,
                    prinitingrolldetailsform,RollDetailsFormset, 
                    ProductionRollDetailsForm,
                    OilPumpingDetailsForm,
                    DailyPouchCuttingDetailsForm,
                    ManualLeakChangeManpowerForm,ManualLeakChangeRollPouchFSForm,
                    )

class home(View):
    def get(self, request):
        breadcrumbs = [
        {'label': 'Home', 'url': '#'}
        ] # Assuming current page doesn't have a URL
        
        context = {
            'breadcrumbs' : breadcrumbs
        }
        
        return render(request, 'Packing/dashboard.html', context)
    
class skudetails(ListView):
    model = branddetails
    template_name = 'Packing/skulist.html' 
    paginate_by = 10
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'SKU\'s', 'url': None},
        {'label': 'SKU List', 'url': None},  # Assuming current page doesn't have a URL
    ]  
    
    def paginate_custom_queryset(self, queryset, page_size,page_param):
        paginator = Paginator(queryset, page_size)
        page = self.request.GET.get(page_param)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        return paginated_queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs

        # Paginate oilcategorydetails
        oilcategorylists = oilcategorydetails.objects.all()
        context['oilcategorylists'] = self.paginate_custom_queryset(oilcategorylists, self.paginate_by, 'page_oil')

        # Paginate skunamedetails
        skunamelists = skunamedetails.objects.all()
        print(skunamelists)
        context['skunamelists'] = self.paginate_custom_queryset(skunamelists, self.paginate_by, 'page_sku')

        # Paginate branddetails
        brandlists = branddetails.objects.all()
        #print("brandlists", brandlists)
        context['brandlists'] = self.paginate_custom_queryset(brandlists, self.paginate_by, 'page_brand')

        context['brandcount'] = brandlists.count()
        context['categorycount'] = oilcategorylists.count()
        context['skucount'] = skunamelists.count()

        return context


    
class filmrolltable(View):
    def get(self, request):
        query = PrintingRollDetail.objects.all().order_by('-updatedat')  # Order by the updated at in descending order
        
        paginator = Paginator(query, 10)  # Paginate by 10 items per page
        page = request.GET.get('page')
        try:
            datatable = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            datatable = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            datatable = paginator.page(paginator.num_pages)
        
        breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Printing', 'url': None},
        {'label': 'Film Roll Table', 'url': None},  # Assuming current page doesn't have a URL
    ] 
        context = {
            'breadcrumbs':breadcrumbs,
            'datatable': datatable
        }
                
        return render(request, 'Packing/printingfilmrolltable.html',context)
    
    
    

class filmrolltableUpdateView(CreateView):
   pass

class filmrolltableDeleteView(DeleteView):
    pass
    
def filmrollentry(request):
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Printing', 'url': None},
        {'label': 'Film Roll Entry', 'url': None},  # Assuming current page doesn't have a URL
    ] 
    if request.method == 'POST':
        priniting_rolldetails_form = prinitingrolldetailsform(request.POST)
        roll_detail_formset = RollDetailsFormset(request.POST)
        if priniting_rolldetails_form.is_valid() and roll_detail_formset.is_valid():
            batch = priniting_rolldetails_form.save()
            roll_detail_formset.instance = batch
            roll_detail_formset.save()
            print("Form Saved")
            return redirect('printingfilmrolltable') 
        
    else:
        priniting_rolldetails_form = prinitingrolldetailsform()
        roll_detail_formset = RollDetailsFormset()
    return render(request, 'Packing/printingfilmrollentry.html',{'printingrolldetailsform1':priniting_rolldetails_form, 'rolldetailsformset':roll_detail_formset, 'breadcrumbs': breadcrumbs})#
    
        
class productionrolltableListView(ListView):
    model = ProductionRollDetails
    template_name = 'Packing/productionrolltable.html'
    context_object_name = 'datatable'
    #paginate_by = 10
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Production', 'url': '/Packing/productionrolltable'},
        {'label': 'Production Table', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context

class productionrolltableCreateView(CreateView):
    model = ProductionRollDetails
    form_class = ProductionRollDetailsForm
    template_name = 'Packing/productionrolltableentry.html'
    success_url = reverse_lazy('productionrolltable')    
    pass
   
class productionrolltableUpdateView(UpdateView):
    model = ProductionRollDetails
    form_class = ProductionRollDetailsForm
    template_name = 'Packing/productionrolltableedit.html'
    success_url = reverse_lazy('productionrolltable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Production', 'url': '/Packing/productionrolltable'},
        {'label': 'Film roll Update', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
    
class productionrolltableDeleteView(DeleteView):
    model = ProductionRollDetails
    template_name = 'Packing/productionrolltabledelete.html'
    success_url = reverse_lazy('productionrolltable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Production', 'url': '/Packing/productionrolltable'},
        {'label': 'Film Roll Delete', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
   
class oilpumpListView(ListView):
    model = OilPumpingDetails
    template_name = 'Packing/oilpumpingtable.html'
    context_object_name = 'datatable'
    #paginate_by = 10
    
    
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Oil Pumping', 'url': '/Packing/oilpumpingtable'},
        {'label': 'Oil Pumping Table', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    pass   
class oilpumpCreateView(CreateView):
    model = OilPumpingDetails
    form_class = OilPumpingDetailsForm
    template_name = 'Packing/oilpumpingentry.html'
    success_url = reverse_lazy('oilpumpingtable')
    
    pass 
class oilpumpUpdateView(UpdateView):
    model = OilPumpingDetails
    form_class = OilPumpingDetailsForm
    template_name = 'Packing/oilpumpingtableedit.html'
    success_url = reverse_lazy('oilpumpingtable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Oil Pumping', 'url': '/Packing/oilpumpingtable'},
        {'label': 'Oil Pumping Edit', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
    pass 
class oilpumpDeleteView(DeleteView):
    model = OilPumpingDetails
    template_name = 'Packing/oilpumpingtabledelete.html'
    success_url = reverse_lazy('oilpumpingtable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Oil Pumping', 'url': '/Packing/oilpumpingtable'},
        {'label': 'Oil Pumping Delete', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
    pass 

class DailyPouchCuttingDetailsListView(ListView):
    model = DailyPouchCuttingDetails
    template_name = 'Packing/dailypouchcuttingtable.html'
    context_object_name = 'datatable'
    paginate_by = 10
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Pouch Cutting', 'url': '/Packing/pouchcuttingtable'},
        {'label': 'Pouch Cutting Table', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
    pass
class DailyPouchCuttingDetailsCreateView(CreateView):
    model = DailyPouchCuttingDetails
    form_class = DailyPouchCuttingDetailsForm
    template_name = 'Packing/dailypouchcuttingentry.html'
    success_url = reverse_lazy('pouchcuttingtable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Pouch Cutting', 'url': '/Packing/pouchcuttingtable'},
        {'label': 'Pouch Cutting Add', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
class DailyPouchCuttingDetailsUpdateView(UpdateView):
    model = DailyPouchCuttingDetails
    form_class = DailyPouchCuttingDetailsForm
    template_name = 'Packing/dailypouchcuttingentry.html'
    success_url = reverse_lazy('pouchcuttingtable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Pouch Cutting', 'url': '/Packing/pouchcuttingtable'},
        {'label': 'Pouch Cutting Update', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
    pass
class DailyPouchCuttingDetailsDeleteView(DeleteView):
    model = DailyPouchCuttingDetails
    template_name = 'Packing/dailypouchcuttingtabledelete.html'
    success_url = reverse_lazy('pouchcuttingtable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Pouch Cutting', 'url': '/Packing/pouchcuttingtable'},
        {'label': 'Pouch Cutting Delete', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
    pass   

class ManualLeakChangeCreateView(CreateView):
    model = ManualLeakChangeManpower
    form_class = ManualLeakChangeManpowerForm
    template_name = 'Packing/manualleakchangetableentry.html'
    success_url = reverse_lazy('manualleakchangetable')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Manual Leak Change', 'url': '/Packing/manualleakchangetable'},
        {'label': 'Leak Change Table Add', 'url': None},  # Assuming current page doesn't have a URL
        ]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['child_formset'] = inlineformset_factory(ManualLeakChangeManpower, ManualLeakChangeRollPouchFS, form=ManualLeakChangeRollPouchFSForm, extra=10)(self.request.POST)
        else:
            data['child_formset'] = inlineformset_factory(ManualLeakChangeManpower, ManualLeakChangeRollPouchFS, form=ManualLeakChangeRollPouchFSForm, extra=10)()
        data['breadcrumbs'] = self.breadcrumbs
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        child_formset = context['child_formset']
        if child_formset.is_valid():
            self.object = form.save()
            child_formset.instance = self.object
            child_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ManualLeakChangeListView(ListView):
    model = ManualLeakChangeRollPouchFS
    template_name = 'Packing/manualleakchangetable.html'
    context_object_name = 'datatable'
    #paginate_by = 10
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Manual Leak Change', 'url': '/Packing/manualleakchangetable'},
        {'label': 'Leak Change Table', 'url': None},  # Assuming current page doesn't have a URL
        ] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        return context
    
  

class ManualLeakChangeUpdateView(UpdateView):
    model = ManualLeakChangeManpower
    form_class = ManualLeakChangeManpowerForm
    template_name = 'Packing/manualleakchangetableedit.html'
    success_url = reverse_lazy('packinghome')
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Manual Leak Change', 'url': '/Packing/manualleakchangetable'},
        {'label': 'Leak Change Table Update', 'url': None},  # Assuming current page doesn't have a URL
        ]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['child_formset'] = inlineformset_factory(ManualLeakChangeManpower, ManualLeakChangeRollPouchFS, form=ManualLeakChangeRollPouchFSForm, extra=10)(self.request.POST)
        else:
            data['child_formset'] = inlineformset_factory(ManualLeakChangeManpower, ManualLeakChangeRollPouchFS, form=ManualLeakChangeRollPouchFSForm, extra=10)()
        data['breadcrumbs'] = self.breadcrumbs
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        child_formset = context['child_formset']
        if child_formset.is_valid():
            self.object = form.save()
            child_formset.instance = self.object
            child_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    
    

class ManualLeakChangeDeleteView(DeleteView):
    model = ManualLeakChangeManpower
    template_name = 'Packing/brandnameedit.html'
    success_url = reverse_lazy('manualleakchangetable')



def autocomplete_skuname(request):
    
    if 'term' in request.GET:
        return JsonResponse({'hi':'hi'})
        print('data received')
        qs = skunamedetails.objects.filter(name__icontains='su')
        names = list()
        for item in qs:
            names.append(item.name)
        return JsonResponse(names, safe=False)
    else:
        print("No term received")  # Print to console/log
    return JsonResponse([], safe=False)

logger = logging.getLogger(__name__)
def toggle(request):
    try:
        btnradio = request.GET.get('btnradio')
        filter_option,dbname = btnradio.split(',')
        #print("option",filter_option)
        #print("dbname",dbname)
        if dbname == "ProductionRollDetails":   
            today = datetime.now().date()
            if filter_option == 'all':
                data = ProductionRollDetails.objects.all()
            elif filter_option == 'today':
                data = ProductionRollDetails.objects.filter(runningdate=today)
            elif filter_option == '7d':
                seven_days_ago = today - timedelta(days=7)
                #print(seven_days_ago)
                data = ProductionRollDetails.objects.filter(runningdate__gte=seven_days_ago)
            elif filter_option == 'last_month':
                last_month_start = today.replace(day=1) - timedelta(days=1)
                last_month_end = today.replace(day=1) - timedelta(days=1)
                data = ProductionRollDetails.objects.filter(runningdate__range=[last_month_start, last_month_end])
            elif filter_option == 'last_3_months':
                three_months_ago = today.replace(day=1) - timedelta(days=1)
                last_three_months_start = three_months_ago - timedelta(days=90)
                data = ProductionRollDetails.objects.filter(runningdate__gte=last_three_months_start)
            elif filter_option == 'last_year':
                last_year_start = today.replace(year=today.year - 1, month=1, day=1)
                last_year_end = today.replace(year=today.year - 1, month=12, day=31)
                data = ProductionRollDetails.objects.filter(runningdate__range=[last_year_start, last_year_end])
            else:
                # Handle invalid filter options
                data = ProductionRollDetails.objects.none()            
            # Log the data for debugging
            logger.info(f'Filtered data: {data}')
            return render(request, 'Packing/productionrolltable_data.html', {'datatable': data})
        
        if dbname == "PrintingRollDetail":   
            today = datetime.now().date()
            if filter_option == 'all':
                data = PrintingRollDetail.objects.all()
            elif filter_option == 'today':
                batchdate = PrintingRollBatch.objects.get(date=today)
                data = PrintingRollDetail.objects.filter(printingrollbatch=batchdate)
            elif filter_option == '7d':
                seven_days_ago = today - timedelta(days=7)
                batchdate = PrintingRollBatch.objects.filter(date__gte=seven_days_ago)
                #print(batchdate)
                data = PrintingRollDetail.objects.filter(printingrollbatch__in=batchdate)
            elif filter_option == 'last_month':
                # last_month_start = today.replace(day=1) - timedelta(days=1)
                # last_month_end = today.replace(day=1) - timedelta(days=1)
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_month_start = last_month_end.replace(day=1)
                batchdate = PrintingRollBatch.objects.filter(date__range=[last_month_start, last_month_end])
                #print(batchdate)
                data = PrintingRollDetail.objects.filter(printingrollbatch__in=batchdate)
            elif filter_option == 'last_3_months':
                # three_months_ago = today.replace(day=1) - timedelta(days=1)
                # last_three_months_start = three_months_ago - timedelta(days=90)
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_3_months_start = last_month_end.replace(day=1) - timedelta(days=2*30)  # Assuming 30 days per month
                last_3_months_end = last_month_end
    
                # Filter PrintingRollBatch objects for the last 3 months
                batchdate = PrintingRollBatch.objects.filter(date__range=[last_3_months_start, last_3_months_end])
                #print(last_3_months_start)
                #print(last_3_months_end)
                
                # Filter PrintingRollDetail objects based on batchdate
                data = PrintingRollDetail.objects.filter(printingrollbatch__in=batchdate)
            elif filter_option == 'last_year':
                # last_year_start = today.replace(year=today.year - 1, month=1, day=1)
                # last_year_end = today.replace(year=today.year - 1, month=12, day=31)
                # data = PrintingRollDetail.objects.filter(date__range=[last_year_start, last_year_end])
                today = date.today()
                last_year_start = today.replace(year=today.year - 1, month=1, day=1)
                last_year_end = last_year_start.replace(month=12, day=31)
                
                # Filter PrintingRollBatch objects for the last year
                batchdate = PrintingRollBatch.objects.filter(date__range=[last_year_start, last_year_end])
                #print(batchdate)
                
                # Filter PrintingRollDetail objects based on batchdate
                data = PrintingRollDetail.objects.filter(printingrollbatch__in=batchdate)
            else:
                # Handle invalid filter options
                data = PrintingRollDetail.objects.none()
            
            # Log the data for debugging
            logger.info(f'Filtered data: {data}')

            return render(request, 'Packing/printingfilmrolltable_data.html', {'datatable': data})
        
        if dbname == "OilPumpingDetails":   
            today = datetime.now().date()
            if filter_option == 'all':
                data = OilPumpingDetails.objects.all()
            elif filter_option == 'today':
                
                data = OilPumpingDetails.objects.filter(date=today)
            elif filter_option == '7d':
                seven_days_ago = today - timedelta(days=7)
                #print(seven_days_ago)
                data = OilPumpingDetails.objects.filter(date__gte=seven_days_ago)
            elif filter_option == 'last_month':
                # last_month_start = today.replace(day=1) - timedelta(days=1)
                # last_month_end = today.replace(day=1) - timedelta(days=1)
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_month_start = last_month_end.replace(day=1)
                batchdate = OilPumpingDetails.objects.filter(date__range=[last_month_start, last_month_end])
                #print(last_month_end)
                #print(last_month_start)
                data = OilPumpingDetails.objects.filter(date__range=[last_month_start, last_month_end])
            elif filter_option == 'last_3_months':
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_3_months_start = last_month_end.replace(day=1) - timedelta(days=2*30)  # Assuming 30 days per month
                last_3_months_end = last_month_end
                print(last_3_months_start)
                print(last_3_months_end)
                data = OilPumpingDetails.objects.filter(date__gte=last_3_months_start)
            elif filter_option == 'last_year':
                last_year_start = today.replace(year=today.year - 1, month=1, day=1)
                last_year_end = today.replace(year=today.year - 1, month=12, day=31)
                data = OilPumpingDetails.objects.filter(date__range=[last_year_start, last_year_end])
            else:
                # Handle invalid filter options
                data = OilPumpingDetails.objects.none()            
            # Log the data for debugging
            logger.info(f'Filtered data: {data}')
            return render(request, 'Packing/oilpumpingtable_data.html', {'datatable': data})
        
        if dbname == "DailyPouchCuttingDetails":   
            today = datetime.now().date()
            if filter_option == 'all':
                data = DailyPouchCuttingDetails.objects.all()
            elif filter_option == 'today':
                
                data = DailyPouchCuttingDetails.objects.filter(date=today)
            elif filter_option == '7d':
                seven_days_ago = today - timedelta(days=7)
                #print(seven_days_ago)
                data = DailyPouchCuttingDetails.objects.filter(date__gte=seven_days_ago)
            elif filter_option == 'last_month':
                # last_month_start = today.replace(day=1) - timedelta(days=1)
                # last_month_end = today.replace(day=1) - timedelta(days=1)
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_month_start = last_month_end.replace(day=1)
                batchdate = DailyPouchCuttingDetails.objects.filter(date__range=[last_month_start, last_month_end])
                #print(last_month_end)
                #print(last_month_start)
                data = DailyPouchCuttingDetails.objects.filter(date__range=[last_month_start, last_month_end])
            elif filter_option == 'last_3_months':
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_3_months_start = last_month_end.replace(day=1) - timedelta(days=2*30)  # Assuming 30 days per month
                last_3_months_end = last_month_end
                # print(last_3_months_start)
                # print(last_3_months_end)
                data = DailyPouchCuttingDetails.objects.filter(date__gte=last_3_months_start)
            elif filter_option == 'last_year':
                last_year_start = today.replace(year=today.year - 1, month=1, day=1)
                last_year_end = today.replace(year=today.year - 1, month=12, day=31)
                data = DailyPouchCuttingDetails.objects.filter(date__range=[last_year_start, last_year_end])
            else:
                # Handle invalid filter options
                data = DailyPouchCuttingDetails.objects.none()            
            # Log the data for debugging
            logger.info(f'Filtered data: {data}')
            return render(request, 'Packing/dailypouchcuttingtable_data.html', {'datatable': data})
        
        if dbname == "ManualLeakChangeRollPouchFS":   
            today = datetime.now().date()
            if filter_option == 'all':
                print("hi")
                data = ManualLeakChangeRollPouchFS.objects.all()
            elif filter_option == 'today':
                manpowerdetails = ManualLeakChangeManpower.objects.filter(date=today)
                #print(leakchangedate)
                data = ManualLeakChangeRollPouchFS.objects.filter(manpower__in=manpowerdetails)
            elif filter_option == '7d':
                seven_days_ago = today - timedelta(days=7)
                manpowerdetails = ManualLeakChangeManpower.objects.filter(date__gte=seven_days_ago)
                #print(batchdate)
                data = ManualLeakChangeRollPouchFS.objects.filter(manpower__in=manpowerdetails)
            elif filter_option == 'last_month':
                # last_month_start = today.replace(day=1) - timedelta(days=1)
                # last_month_end = today.replace(day=1) - timedelta(days=1)
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_month_start = last_month_end.replace(day=1)
                manpowerdetails = ManualLeakChangeManpower.objects.filter(date__range=[last_month_start, last_month_end])
                #print(batchdate)
                data = ManualLeakChangeRollPouchFS.objects.filter(manpower__in=manpowerdetails)
            elif filter_option == 'last_3_months':
                # three_months_ago = today.replace(day=1) - timedelta(days=1)
                # last_three_months_start = three_months_ago - timedelta(days=90)
                today = date.today()
                last_month_end = today.replace(day=1) - timedelta(days=1)
                last_3_months_start = last_month_end.replace(day=1) - timedelta(days=2*30)  # Assuming 30 days per month
                last_3_months_end = last_month_end
    
                # Filter PrintingRollBatch objects for the last 3 months
                manpowerdetails = ManualLeakChangeManpower.objects.filter(date__range=[last_3_months_start, last_3_months_end])
                #print(last_3_months_start)
                #print(last_3_months_end)
                
                # Filter PrintingRollDetail objects based on batchdate
                data = ManualLeakChangeRollPouchFS.objects.filter(manpower__in=manpowerdetails)
            elif filter_option == 'last_year':
                # last_year_start = today.replace(year=today.year - 1, month=1, day=1)
                # last_year_end = today.replace(year=today.year - 1, month=12, day=31)
                # data = PrintingRollDetail.objects.filter(date__range=[last_year_start, last_year_end])
                today = date.today()
                last_year_start = today.replace(year=today.year - 1, month=1, day=1)
                last_year_end = last_year_start.replace(month=12, day=31)
                
                # Filter PrintingRollBatch objects for the last year
                manpowerdetails = ManualLeakChangeManpower.objects.filter(date__range=[last_year_start, last_year_end])
                #print(batchdate)
                
                # Filter PrintingRollDetail objects based on batchdate
                data = ManualLeakChangeRollPouchFS.objects.filter(manpower__in=manpowerdetails)
            else:
                # Handle invalid filter options
                data = ManualLeakChangeRollPouchFS.objects.none()
            
            # Log the data for debugging
            logger.info(f'Filtered data: {data}')

            return render(request, 'Packing/manualleakchangetable_data.html', {'datatable': data})
    except Exception as e:
        logger.error(f'Error in toggle view: {e}')
        # Handle exceptions, e.g., log the error
        return render(request, 'Packing/oilpumpingtable_data.html', {'datatable': []})
    
    
    #return render(f'Selected choice: {getdata}')
    
    #data = ProductionRollDetails.objects.all()
    #print(data)
    #html_data = render_to_string('Packing/printingfilmrolltable_data.html', {'datatable': data})

    # Return the HTML fragment as JSON response
    # return JsonResponse({'html': html_data})
    #return JsonResponse({'html': 'html_data'})
    # def get(self, request):
    #     query = ProductionRollDetails.objects.all().order_by('-updatedat')  # Order by the updated at in descending order
    #     breadcrumbs = [
    #     {'label': 'Home', 'url': '/Packing'},
    #     {'label': 'Production', 'url': None},
    #     {'label': 'Production Roll Table', 'url': None},  # Assuming current page doesn't have a URL
    # ] 
    #     context = {
    #         'breadcrumbs':breadcrumbs,
    #         'datatable': query
    #     }
            
    #     return render(request, 'Packing/productionrolltable.html',context)



# class GenericListView(ListView):
#     template_name = 'Packing/generictemplate.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['view'] = {
#             'action': 'list',
#             'create_url': reverse_lazy(f'{self.model._meta.model_name}-create'),
#             'model_name': self.model._meta.verbose_name.capitalize(),
#         }
#         return context

# class GenericCreateView(CreateView):
#     template_name = 'Packing/generic_template.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['view'] = {
#             'action': 'form',
#             'submit_label': 'Create',
#         }
#         return context

# class GenericUpdateView(UpdateView):
#     template_name = 'Packing/generic_template.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['view'] = {
#             'action': 'form',
#             'submit_label': 'Update',
#         }
#         return context

# class GenericDeleteView(DeleteView):
#     template_name = 'Packing/generic_template.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['view'] = {
#             'action': 'delete',
#             'cancel_url': reverse_lazy(f'{self.model._meta.model_name}-list'),
#         }
#         return context

#     def get_success_url(self):
#         return reverse_lazy(f'{self.model._meta.model_name}-list')

# class BrandListView(GenericListView):
#     model = branddetails

# class BrandCreateView(GenericCreateView):
#     model = branddetails
#     fields = ['brandname']

# class BrandUpdateView(GenericUpdateView):
#     model = branddetails
#     fields = ['brandname']

# class BrandDeleteView(GenericDeleteView):
#     model = branddetails

# class OilCategoryListView(GenericListView):
#     model = oilcategorydetails

# class OilCategoryCreateView(GenericCreateView):
#     model = oilcategorydetails
#     fields = ['brandname', 'oilcategoryname']

# class OilCategoryUpdateView(GenericUpdateView):
#     model = oilcategorydetails
#     fields = ['brandname', 'oilcategoryname']

# class OilCategoryDeleteView(GenericDeleteView):
#     model = oilcategorydetails

# class SkuNameListView(GenericListView):
#     model = skunamedetails

# class SkuNameCreateView(GenericCreateView):
#     model = skunamedetails
#     fields = ['oilcategoryname', 'skuname', 'skucode']

# class SkuNameUpdateView(GenericUpdateView):
#     model = skunamedetails
#     fields = ['oilcategoryname', 'skuname', 'skucode']

# class SkuNameDeleteView(GenericDeleteView):
#     model = skunamedetails

# Create your views here.