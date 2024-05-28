from django.urls import path, include
from .views import ( home,
                    skudetails, 
                    filmrolltable, filmrollentry, filmrolltableUpdateView,filmrolltableDeleteView,
                    productionrolltableListView,productionrolltableUpdateView,productionrolltableDeleteView,productionrolltableCreateView,
                    dispatchstocktableListView,
                    oilpumpListView,oilpumpCreateView,oilpumpUpdateView,oilpumpDeleteView,
                    DailyPouchCuttingDetailsListView,DailyPouchCuttingDetailsCreateView,DailyPouchCuttingDetailsUpdateView,DailyPouchCuttingDetailsDeleteView,
                    ManualLeakChangeListView,ManualLeakChangeCreateView,ManualLeakChangeUpdateView,ManualLeakChangeDeleteView,
                    autocomplete_skuname,toggle,download_printingrolltable,download_productionrolltable,download_oilpumpingtable,download_pouchcuttingtable,download_manualleakchangetable,
                    chart_data,chart_view,download_ppsrtable,
                    PPSRListView,PPSRCreateView,PPSRUpdateView,PPSRDeleteView,)


urlpatterns = [
    path('',home.as_view(),name='packinghome'),
    path('skulists/',skudetails.as_view(),name="skulists"),
    #-------------------------------------------------Printing------------------------------------------------
    path('printingfilmrolltable/',filmrolltable.as_view(),name='printingfilmrolltable'),
    path('printingfilemrolltable/<pk>/edit',filmrolltableUpdateView.as_view(),name='printingfilmrolltable_update'),
    path('printingfilmrolltable/<pk>/delete',filmrolltableDeleteView.as_view(),name='printingfilmrolltable_delete'),
    path('printingfilmrollentry/',filmrollentry,name='filmrollentry'),
    path('printingfilmrolltable/download_printingrolltable', download_printingrolltable, name='download_printingrolltable'),
    #_________________________________________________________________________________________________________
    
    #----------------------------------------------------Production--------------------------------------------
    #path('select2/', include('django_select2.urls')),
    path('productionrolltable/',productionrolltableListView.as_view(),name='productionrolltable'),
    path('productionrolltable/newentry',productionrolltableCreateView.as_view(),name='productionrolltable_entry'),
    path('productionrolltable/<pk>/edit',productionrolltableUpdateView.as_view(),name='productionrolltable_update'),
    path('productionrolltable/<pk>/delete',productionrolltableDeleteView.as_view(),name='productionrolltable_delete'),
    path('dispatchstocktable/',dispatchstocktableListView.as_view(),name='dispatchstocktable'),
    path('productionrolltable/download_productionrolltable', download_productionrolltable, name='download_productionrolltable'),
    
    #___________________________________________________________________________________________________________
    
    #---------------------------------------------------Oil Pumping---------------------------------------------
    path('oilpumpingtable/',oilpumpListView.as_view(),name='oilpumpingtable'),
    path('oilpumpingtable/newentry/',oilpumpCreateView.as_view(),name='oilpumpingtable_entry'),
    path('oilpumpingtable/<pk>/edit/',oilpumpUpdateView.as_view(),name='oilpumpingtable_update'),
    path('oilpumpingtable/<pk>/delete/',oilpumpDeleteView.as_view(),name='oilpumpingtable_delete'),
    path('oilpumpingtable/download_oilpumpingtable', download_oilpumpingtable, name='download_oilpumpingtable'),
    #___________________________________________________________________________________________________________
    
    #---------------------------------------------------Pouch Cutting---------------------------------------------
    path('pouchcuttingtable/',DailyPouchCuttingDetailsListView.as_view(),name='pouchcuttingtable'),
    path('pouchcuttingtable/newentry/',DailyPouchCuttingDetailsCreateView.as_view(),name='pouchcuttingtable_entry'),
    path('pouchcuttingtable/<pk>/edit/',DailyPouchCuttingDetailsUpdateView.as_view(),name='pouchcuttingtable_update'),
    path('pouchcuttingtable/<pk>/delete/',DailyPouchCuttingDetailsDeleteView.as_view(),name='pouchcuttingtable_delete'),
    path('pouchcuttingtable/download_pouchcuttingtable', download_pouchcuttingtable, name='download_pouchcuttingtable'),
    #___________________________________________________________________________________________________________
    
    #---------------------------------------------Manual Pouch Leak Change --------------------------------------
    path('manualleakchangetable/',ManualLeakChangeListView.as_view(),name='manualleakchangetable'),
    path('manualleakchangetable/newentry',ManualLeakChangeCreateView.as_view(),name='manualleakchangetable_entry'),
    path('manualleakchangetable/<pk>/edit',ManualLeakChangeUpdateView.as_view(),name='manualleakchangetable_update'),
    path('manualleakchangetable/<pk>/delete',ManualLeakChangeDeleteView.as_view(),name='manualleakchangetable_delete'),
    path('manualleakchangetable/download_manualleakchangetable', download_manualleakchangetable, name='download_manualleakchangetable'), 
    
    #____________________________________________________________________________________________________________
    
    
    path('autocomplete-skuname/', autocomplete_skuname, name='autocomplete_skuname'), # try to autocomplete not working
    
    #------------------------------------------------HTMX Table Filter--------------------------------------------
    path('printingfilmrolltable/Packing/toggle',toggle,name="toggle"),
    #_____________________________________________________________________________________________________________
    
    
    #-------------------------------------------------------------------------------------------------------------------
    path('chart-data/', chart_data, name='chart_data'),
    path('chart/', chart_view, name='chart_view'),   
    #____________________________________________________________________________________________________________________________
    
    
    #------------------------------------------------PPSR------------------------------------------------------
    path('ppsrtable',PPSRListView.as_view(),name='ppsrtable'),
    path('ppsrtable/newentry',PPSRCreateView.as_view(),name='ppsrtable_entry'),
    path('ppsrtable/<pk>/edit',PPSRUpdateView.as_view(),name='ppsrtable_update'),
    path('ppsrtable/<pk>/delete',PPSRDeleteView.as_view(),name='ppsrtable_delete'),
    path('ppsrtable/download_ppsrtable', download_ppsrtable, name='download_ppsrtable'),
    
    #__________________________________________________________________________________________________________
    
    
    # path('brands/', BrandListView.as_view(), name='branddetails-list'),
    # path('brands/new/', BrandCreateView.as_view(), name='branddetails-create'),
    # path('brands/<pk>/edit', BrandUpdateView.as_view(), name='branddetails-update'),
    # path('brands/<pk>/delete/', BrandDeleteView.as_view(), name='branddetails-delete'),

    # path('oilcategories/', OilCategoryListView.as_view(), name='oilcategorydetails-list'),
    # path('oilcategories/new/', OilCategoryCreateView.as_view(), name='oilcategorydetails-create'),
    # path('oilcategories/<pk>/edit', OilCategoryUpdateView.as_view(), name='oilcategorydetails-update'),
    # path('oilcategories/<pk>/delete/', OilCategoryDeleteView.as_view(), name='oilcategorydetails-delete'),

    # path('skunames/', SkuNameListView.as_view(), name='skunamedetails-list'),
    # path('skunames/new/', SkuNameCreateView.as_view(), name='skunamedetails-create'),
    # path('skunames/<pk>/edit', SkuNameUpdateView.as_view(), name='skunamedetails-update'),
    # path('skunames/<pk>/delete/', SkuNameDeleteView.as_view(), name='skunamedetails-delete'),



]
