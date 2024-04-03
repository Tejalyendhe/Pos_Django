from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    # dashboards
    path('dashboard/',views.dashboard, name='dashboard'),
    path('report/',views.report, name='report'),
    path('view_inward/',views.view_inward, name='view_inward'),
    path('view_invoice/',views.view_invoice, name='view_invoice'),
    path('view_packing/',views.view_packing, name='view_packing'),
    path('view_exception/',views.view_exception, name='view_exception'),
    path('view_product/<str:inw>/',views.view_product, name='view_product'),
    path('view_product_inv/<str:inv>/',views.view_product_inv, name='view_product_inv'),
    path('load_table_data/', views.load_table_data, name='load_table_data'),
    path('loadinvoice_table_data/', views.loadinvoice_table_data, name='loadinvoice_table_data'),
    path('mark_as_done/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_done_inv/', views.mark_as_done_inv, name='mark_as_done_inv'),

    # 
    path('search_supplier/', views.search_supplier, name="search_supplier"),
    
    # search_barcode
    path('search_barcode/', views.search_barcode, name="search_barcode"),

    # update_price
     path('update_price/', views.update_price, name="update_price"),
    
    #take_pic
    path('take_pic/', views.take_pic, name="take_pic"),
    
    # generate_bill
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('save_bill/', views.save_bill, name='save_bill'),
    path('view_bill/', views.view_bill, name='view_bill'),
    path('fetch_dispatch_data/', views.fetch_dispatch_data, name='fetch_dispatch_data'),
    path('bill_print/<str:sale_no>', views.bill_print, name='bill_print'),

    # analysis
    path('analysis/', views.AnalysisView.analysis, name='analysis'),
    path('item-wise-analysis/', views.AnalysisView.itemWise, name='item-wise-analysis'),
    path('item-wise-analysis/<str:item>', views.AnalysisView.itemWiseData, name='item-wise-data'),
    path('price-wise-analysis/', views.AnalysisView.priceWise, name='price-wise-analysis'),
    path('supplier-wise-analysis/', views.AnalysisView.supplierWise, name='supplier-wise-analysis'),
    path('city-wise-analysis/', views.AnalysisView.cityWise, name='city-wise-analysis'),

    # view master input
    # path('view_master_input/', views.view_master_input, name="view_master_input"),


    # login
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('get_users_by_store/<str:si>', views.get_users_by_store, name='get_users_by_store'),
    path('validate_password/', views.validate_password, name='validate_password'),
    path("logout/", views.CustomLogoutView.as_view(), name='logout'),

    path('handle_scanned_data/', views.handle_scanned_data, name='handle_scanned_data'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)