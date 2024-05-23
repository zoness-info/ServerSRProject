from django.urls import path, include
from .views import ( home,
                    skudetails, filmrolltable, filmrollentry, productionrolltableListView,productionrolltableUpdateView,productionrolltableDeleteView
    # BrandListView, BrandCreateView, BrandUpdateView, 
    # BrandDeleteView,OilCategoryListView, OilCategoryCreateView, 
    # OilCategoryUpdateView, OilCategoryDeleteView,SkuNameListView, 
    # SkuNameCreateView, SkuNameUpdateView, SkuNameDeleteView
)

urlpatterns = [
    path('',home.as_view(),name='packinghome'),
    
    path('skulists/',skudetails.as_view(),name="skulists"),
    path('filmrolltable/',filmrolltable.as_view(),name='filmrolltable'),
    path('filmrollentry/',filmrollentry,name='filmrollentry'),
    #path('select2/', include('django_select2.urls')),
    path('productionrolltable/',productionrolltableListView.as_view(),name='productionrolltable'),
    path('productionrolltable/<pk>/edit',productionrolltableUpdateView.as_view(),name='productionrolltable_update'),
    path('productionrolltable/<pk>/delete',productionrolltableDeleteView.as_view(),name='productionrolltable_delete'),
    
    
    
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
