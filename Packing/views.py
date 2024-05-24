from django.shortcuts import get_object_or_404, redirect, render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import branddetails, oilcategorydetails, skunamedetails, PrintingRollBatch, PrintingRollDetail, ProductionRollDetails
from .forms import branddetailsform,prinitingrolldetailsform,RollDetailsFormset, ProductionRollDetailsForm

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
    #context_object_name = 'oilbrands'
    # form_class = supplierForm
    # success_url = '/stores/supplier'
    # success_message = "Supplier details has been updated successfully" 
    paginate_by = 10
    breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'SKU\'s', 'url': None},
        {'label': 'SKU List', 'url': None},  # Assuming current page doesn't have a URL
    ]  
     
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs
        context['oilcategorylists'] = oilcategorydetails.objects.all()
        context['skunamelist'] = skunamedetails.objects.all()
        context['brandcount'] = branddetails.objects.count()
        context['categorycount'] = context['oilcategorylists'].count()
        context['skucount'] = context['skunamelist'].count()
        return context


    
class filmrolltable(View):
    def get(self, request):
        query = PrintingRollDetail.objects.all().order_by('-updatedat')  # Order by the updated at in descending order
        breadcrumbs = [
        {'label': 'Home', 'url': '/Packing'},
        {'label': 'Printing', 'url': None},
        {'label': 'Film Roll Table', 'url': None},  # Assuming current page doesn't have a URL
    ] 
        context = {
            'breadcrumbs':breadcrumbs,
            'datatable': query
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
            return redirect('filmrolltable') 
        
    else:
        priniting_rolldetails_form = prinitingrolldetailsform()
        roll_detail_formset = RollDetailsFormset()
    return render(request, 'Packing/printingfilmrollentry.html',{'printingrolldetailsform1':priniting_rolldetails_form, 'rolldetailsformset':roll_detail_formset, 'breadcrumbs': breadcrumbs})#
    
        
class productionrolltableListView(ListView):
    model = ProductionRollDetails
    template_name = 'Packing/productionrolltable.html'
    context_object_name = 'datatable'
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