from django.urls import path, include
from .views import ( home,
                    skudetails, 
                    filmrolltable, filmrollentry, filmrolltableUpdateView,filmrolltableDeleteView,printingfilmrollavailability,filmrollavilcheck,
                    productionrolltableListView,productionrolltableUpdateView,productionrolltableDeleteView,productionrolltableCreateView,
                    dispatchstocktableListView,download_dispatchstocktable,
                    oilpumpListView,oilpumpCreateView,oilpumpUpdateView,oilpumpDeleteView,
                    DailyPouchCuttingDetailsListView,DailyPouchCuttingDetailsCreateView,DailyPouchCuttingDetailsUpdateView,DailyPouchCuttingDetailsDeleteView,
                    ManualLeakChangeListView,ManualLeakChangeCreateView,ManualLeakChangeUpdateView,ManualLeakChangeDeleteView,
                    autocomplete_skuname,toggle,
                    download_printingrolltable,download_productionrolltable,download_oilpumpingtable,download_pouchcuttingtable,download_manualleakchangetable,
                    chart_data,chart_view,download_expvsacttable,
                    ExpVsActDetailsListView,ExpVsActDetailsCreateView,ExpVsActDetailsUpdateView,ExpVsActDetailsDeleteView,
                    ppsr_details_view,ppsr_details_edit,PPSRDetailsListView,PPSRDetailsCreateView,PPSRDetailsUpdateView,PPSRDetailsDeleteView,
                    SRDailyStockPETJARUpdateView,DailyPETJARstocklist,
                    DailystockPouchList,DailystockPouchUpdate,DailyStockSRFull,
                    DispatchReqVsStockUpdate,DispatchReqVsStockView,
                    CalenderView,
                    )


urlpatterns = [
    path('',home.as_view(),name='packinghome'),
    path('skulists/',skudetails.as_view(),name="skulists"),
    #-------------------------------------------------Printing------------------------------------------------
    path('printingfilmrolltable/',filmrolltable.as_view(),name='printingfilmrolltable'),
    path('printingfilemrolltable/<pk>/edit',filmrolltableUpdateView.as_view(),name='printingfilmrolltable_update'),
    path('printingfilmrolltable/<pk>/delete',filmrolltableDeleteView.as_view(),name='printingfilmrolltable_delete'),
    path('printingfilmrolltable/printingfilmrollentry/',filmrollentry,name='filmrollentry'),
    path('printingfilmrolltable/download_printingrolltable', download_printingrolltable, name='download_printingrolltable'),
    path('printingfilmrolltable/availability',printingfilmrollavailability,name='printingfilmrollavailability'),
    path('printingfilmrolltable/availcheck',filmrollavilcheck,name='filmrollavilcheck'),
    #_________________________________________________________________________________________________________
    
    #----------------------------------------------------MIS--------------------------------------------
    #path('select2/', include('django_select2.urls')),
    path('MIS/productionrolltable',productionrolltableListView.as_view(),name='productionrolltable'),
    path('MIS/newentry',productionrolltableCreateView.as_view(),name='productionrolltable_entry'),
    path('MIS/<pk>/edit',productionrolltableUpdateView.as_view(),name='productionrolltable_update'),
    path('MIS/<pk>/delete',productionrolltableDeleteView.as_view(),name='productionrolltable_delete'),    
    path('MIS/download_productionrolltable', download_productionrolltable, name='download_productionrolltable'),    
    path('MIS/dispatchstocktable/',dispatchstocktableListView.as_view(),name='dispatchstocktable'),
    path('MIS/dispatchstocktable/download_dispatchstocktable', download_dispatchstocktable, name='download_dispatchstocktable'),
    path('MIS/dispatchreqvsstockview',DispatchReqVsStockView.as_view(),name='dispatchreqvsstockview'),
    #path('MIS/dispatchreqvsstockview/download',DispatchReqVsStockView.as_view(), {'action': 'download_excel'},name='dispatchreqvsstockviewdownload'),
    path('MIS/dispatchreqvsstockview/update',DispatchReqVsStockUpdate.as_view(),name='dispatchreqvsstockupdate'),
    path('MIS/ppsrtable',PPSRDetailsListView.as_view(),name='ppsrtable'),
    #path('productionrolltable/ppsrtable/newentry',PPSRDetailsCreateView.as_view(),name='ppsrtable_entry'),
    path('MIS/ppsrtable/<pk>/edit',PPSRDetailsUpdateView.as_view(),name='ppsrtable_update'),
    path('MIS/ppsrtable/<pk>/delete',PPSRDetailsDeleteView.as_view(),name='ppsrtable_delete'),
    
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
    
    
    #------------------------------------------------ExpVsActDetails------------------------------------------------------
    path('expvsacttable',ExpVsActDetailsListView.as_view(),name='expvsacttable'),
    path('expvsacttable/newentry',ExpVsActDetailsCreateView.as_view(),name='expvsacttable_entry'),
    path('expvsacttable/<pk>/edit',ExpVsActDetailsUpdateView.as_view(),name='expvsacttable_update'),
    path('expvsacttable/<pk>/delete',ExpVsActDetailsDeleteView.as_view(),name='expvsacttable_delete'),
    path('expvsacttable/download_expvsacttable', download_expvsacttable, name='download_expvsacttable'),    
    #__________________________________________________________________________________________________________
    
    #--------------------------------------------------Stock-------------------------------------------------------
    path('stock/dailypetjarlist',DailyPETJARstocklist.as_view(),name='dailypetjarstocklist'),
    path('stock/dailypetjarstockupdate',SRDailyStockPETJARUpdateView.as_view(),name='dailypetjarstockupdate'),
    path('stock/dailypouchstocklist',DailystockPouchList.as_view(),name='dailypouchstocklist'),
    path('stock/dailypouchstockupdate',DailystockPouchUpdate.as_view(),name='dailypochstockupdate'),
    path('stock/dailystockSRFull',DailyStockSRFull.as_view(),name='DailyStockSRFull'),
    #_____________________________________________________________________________________________________________________
    
    path('ppsr-details/', ppsr_details_view, name='ppsr_details'),
    path('ppsrtable/newentry',ppsr_details_edit,name='ppsrtable_entry'),
    
    path('calender/',CalenderView.as_view(),name='calenderview'),
    
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
