from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('dispatch_data/<str:dn>/<str:un>/<str:up>', views.dispatch_data, name='dispatch_data'),
    path('add_dispatch_data', views.add_dispatch_data, name='add_dispatch_data'),
    path('get_dispatch_data', views.get_dispatch_data, name='get_dispatch_data'),
    path('get_dispatch_numbers', views.get_dispatch_numbers, name='get_dispatch_numbers'),
    path('add_supplier_data', views.add_supplier_data, name='add_supplier_data'),
    path('supplier_api/', views.supplier_api, name="supplier_api"),

    #user apis
    path('create_new_user', views.create_new_user, name='create_new_user'),
    path('get_user_byStore', views.get_user_byStore, name='get_user_byStore'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('get_user_data', views.get_user_data, name='get_user_data'),

    # sales api
    path('push_sales_data', views.push_sales_data, name='push_sales_data'),
    path('get_sales_data/<str:sn>', views.get_sales_data, name='get_sales_data'),
    path('checkPost', views.checkPost, name='checkPost'),
    path('fetch_by_barcode', views.fetch_by_barcode, name='fetch_by_barcode'),

    # price update api
    path('get_updated_price', views.get_updated_price, name='get_updated_price'),
    path('save_updated_price', views.save_updated_price, name='save_updated_price'),


    # pos   
    path('pos/', include('pos.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)