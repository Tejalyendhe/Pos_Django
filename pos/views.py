from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from api.models import Dispatch_data,DispacthPostUser,StoreType,SaleData,Sale, Supplier,UserType
from django.db.models import Sum 
from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import ItemWithoutLabel,BillDiscount
from api.serializer import SaleDataSerializer, SupplierSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
import traceback

@login_required(login_url='/pos/login')
def dashboard(request):
    return render(request, 'pos/dashboard.html')

def report(request):
    return render(request, 'pos/report.html')

# @cache_page(60 * 30)  # Cache the view for 30 minutes
def view_inward(request):
    return render(request, 'pos/report/view_inward.html')

def view_invoice(request):
    return render(request, 'pos/report/view_invoice.html')

def load_table_data(request):
    unique_inward_numbers = Dispatch_data.objects.values_list('Inward_no', flat=True).order_by('-created_date').distinct()
    # Create a list to store the data for the table
    table_data = []
    # Iterate through unique Inward_no values
    for inward_number in unique_inward_numbers:
        # Filter Dispatch_data by Inward_no
        data_for_inward = Dispatch_data.objects.filter(Inward_no=inward_number)
        # Get unique Supplier Names and Bill Numbers for the Inward_no
        supplier_names = ', '.join(data_for_inward.values_list('supplier', flat=True).distinct())
        bill_numbers = ', '.join(data_for_inward.values_list('Bill_no', flat=True).distinct())
        distpatch_numbers = ', '.join(data_for_inward.values_list('distpatch_no__distpatch_no', flat=True).distinct())
        # Calculate the total Qty for the Inward_no
        total_packed_qty = data_for_inward.aggregate(total_packed_qty=Sum('packed_quantity'))['total_packed_qty']
        total_inward_qty = data_for_inward.aggregate(total_inward_qty=Sum('Qty'))['total_inward_qty']
        total_greturn_qty = data_for_inward.aggregate(total_greturn_qty=Sum('greturn'))['total_greturn_qty']
        Invoice_No=', '.join(data_for_inward.values_list('Invoice_No', flat=True).distinct())
        
        # print(inward_number,total_inward_qty)
        created_date = data_for_inward.first().created_date

        # Append the data to the table_data list
        table_data.append({
            'Inward_no': inward_number,
            'Supplier_names': supplier_names,
            'Bill_numbers': bill_numbers,
            'Distpatch_numbers': distpatch_numbers,
            'Total_packed_qty': total_packed_qty,
            'Total_inward_qty':total_inward_qty,
            'Total_greturn_qty':total_greturn_qty,
            'Created_date': created_date,
            'Invoice_No':Invoice_No,
        })
    return JsonResponse({'table_data': table_data})

from collections import OrderedDict
def loadinvoice_table_data(request):
    invoice_numbers = Dispatch_data.objects.exclude(created_date__isnull=True, Invoice_No__isnull=True).values_list('Invoice_No', flat=True).order_by('-created_date')
    unique_invoice_numbers = list(OrderedDict.fromkeys(invoice_numbers))
    # Create a list to store the data for the table
    table_data = []
    # Iterate through unique Invoice_no values
    for invoice_number in unique_invoice_numbers:
       
        # Filter Dispatch_data by Invoice_no
        data_for_invoice = Dispatch_data.objects.filter(Invoice_No=invoice_number)
        # Get unique Supplier Names and Bill Numbers for the Invoice_no
        
        distpatch_numbers = ', '.join(data_for_invoice.values_list('distpatch_no__distpatch_no', flat=True).distinct())
        # Calculate the total Qty for the Invoice_no
        total_packed_qty = data_for_invoice.aggregate(total_packed_qty=Sum('packed_quantity'))['total_packed_qty']
        total_inward_qty = data_for_invoice.aggregate(total_inward_qty=Sum('Qty'))['total_inward_qty']
        total_greturn_qty = data_for_invoice.aggregate(total_greturn_qty=Sum('Qty'))['total_greturn_qty']
        # print(invoice_number,total_inward_qty)
        created_date = data_for_invoice.first().created_date
        # Append the data to the table_data list
        table_data.append({
            'Invoice_No': invoice_number,
            'Distpatch_numbers': distpatch_numbers,
            'Total_packed_qty': total_packed_qty,
            'Total_inward_qty':total_inward_qty,
            'Total_greturn_qty':total_greturn_qty,
            'Created_date': created_date,
        })
    return JsonResponse({'table_data': table_data})


def mark_as_done(request):
    inw = request.POST.get('inw_no')
    try:
        for inws in Dispatch_data.objects.filter(Inward_no=inw):
            if inws.Qty > 0:
                inws.Exception_quantity=float(inws.Exception_quantity)+float(inws.Qty)
                inws.Qty=0
                inws.save()
        return JsonResponse({'resp': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'resp': 402})
    
def mark_as_done_inv(request):
    inv = request.POST.get('inv_no')
    try:
        for invs in Dispatch_data.objects.filter(Invoice_No=inv):
            if invs.Qty > 0:
                invs.Exception_quantity=float(invs.Exception_quantity)+float(invs.Qty)
                invs.Qty=0
                invs.save()
        return JsonResponse({'resp': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'resp': 402})
    
def view_packing(request):
    return render(request, 'pos/report/view_packing.html')

def view_exception(request):
    return render(request, 'pos/report/view_exception.html')

def view_product(request,inw):
    context = {
        'table_data': Dispatch_data.objects.filter(Inward_no=inw)
    }
    return render(request, 'pos/report/view_product.html', context)

def view_product_inv(request,inv):
    context = {
        'table_data': Dispatch_data.objects.filter(Invoice_No=inv)
    }
    return render(request, 'pos/report/view_invoice_report.html', context)

# login
def login(request):
    context={
        'stores':StoreType.objects.all(),
    }
    return render(request, 'pos/partials/pages-login.html',context)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to '/pos' after logging out

    def get_next_page(self):
        next_page = super().get_next_page()
        if next_page:
            return next_page
        return self.next_page
    
from django.core.serializers import serialize
import json
def get_users_by_store(request, si):
    # Retrieve the users and serialize them to JSON
    users = User.objects.filter(usertype__user_store=StoreType.objects.get(pk=si)).exclude(is_staff=True)
    serialized_users = serialize('json', users)

    # Parse the serialized data
    user_list = json.loads(serialized_users)
    data = {
        'users': user_list,
    }
    return JsonResponse(data)

def validate_password(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password') 
        print(user_id,password)
        try:
            user = auth.authenticate(username=User.objects.get(pk=user_id).username, password=password)
            if user is not None:
                auth.login(request, user)  
                return JsonResponse({'valid': True})
            else:
                return JsonResponse({'valid': False})
        except Exception as e:
            return JsonResponse({'valid': False})

    return JsonResponse({'valid': False})



# added by sarvesh - 26-12-23
@login_required(login_url='/pos/login')
def generate_bill(request):
    context={
        'items':ItemWithoutLabel.objects.all(),
        'discounts':BillDiscount.objects.all().order_by('position')
    }
    return render(request, 'pos/main/generate_bill.html',context)


@login_required(login_url='/pos/login')
def view_bill(request):
    sale_data = SaleData.objects.all().order_by('-id')
    serializer = SaleDataSerializer(sale_data, many=True)
    
    context = {
        'sale_data': serializer.data
    }
    return render(request, 'pos/main/view_bill.html', context)

@login_required(login_url='/pos/login')
def fetch_dispatch_data(request):
    barcode = request.GET.get('barcode', '')
    dispatch_data = Dispatch_data.objects.filter(Unique_no=barcode)
    if dispatch_data:
        data = {
            'Headline': dispatch_data.first().Headline,
            'Qty': dispatch_data.aggregate(Sum('Label_qty'))['Label_qty__sum'],
            'Rate': dispatch_data.first().Rate,
            'Code': f'{dispatch_data.first().Calculation} - {dispatch_data.first().Cipher}',
            'supplier':dispatch_data.first().supplier,
        }
        return JsonResponse(data)
    
    else:
        return JsonResponse({'error': 'Barcode not found'})


from django.shortcuts import get_object_or_404

@login_required(login_url='/pos/login')
def save_bill(request):
    data = {}
    if request.method == 'POST':
        try:
        # Access the posted data
            barcode_list = request.POST.getlist('barcode[]')
            item_list = request.POST.getlist('item[]')
            qty_list = request.POST.getlist('qty[]')
            rate_list = request.POST.getlist('rate[]')
            total_list = request.POST.getlist('total[]')

            # Extract supplier information from the request
            supplier_name = request.POST.get('supplier', '')
            # Generate a unique sale number
            store_name = StoreType.objects.get(id=request.POST.get('store_id', '')) if request.POST.get('store_id', '') else UserType.objects.filter(
                user=request.user).first().user_store.first().store
            sale_number = generate_unique_sale_number()

            # Save the SaleData instance with supplier information
            sale_data = SaleData(
                user=request.user if request.user else '',
                saleNumber=sale_number,
                storeName=store_name,
                saleTotal=request.POST.get('grand_total', ''),
                saleDiscount=request.POST.get('discount', ''),
                saleCard=request.POST.get('cardInput', ''),
                saleCash=request.POST.get('cashInput', ''),
                salePoints=request.POST.get('pointsInput', ''),
                saleBalance=request.POST.get('balance', ''),
                isNotExchange=request.POST.get('noExchangeRefund', ''), 
            )
            sale_data.save()

            # Save the individual Sale instances
            for barcode, item, qty, rate, total in zip(barcode_list, item_list, qty_list, rate_list, total_list):
                if barcode != '':
                    # Fetch Dispatch_data instance and retrieve supplier information
                    Sale.objects.create(
                        salenumber=sale_data,
                        uniqueNumber=barcode,
                        headline=item,
                        rowQty=qty,
                        rowRate=rate,
                        rowTotal=total,
                        supplier= supplier_name  
                    )

            data['sale_no'] = sale_number

            return JsonResponse(data, content_type="application/json")
        except Exception as e:
            traceback.print_exc()
            return HttpResponse("An error occurred. Please check the server logs for more information.", status=500)
    return HttpResponse("Invalid request")



# added by sarvesh 05-01-23
from django.utils import timezone
import pytz

@login_required(login_url='/pos/login')
def bill_print(request, sale_no):
    sale_data = get_object_or_404(SaleData, saleNumber=sale_no)
    sale_items = Sale.objects.filter(salenumber__saleNumber=sale_no)
    sale_data.salesCreatedDate = timezone.localtime(sale_data.salesCreatedDate, timezone=pytz.timezone('Europe/London'))

    context = {
        'sale_data': sale_data,
        'sale_items': sale_items,
    }
    return render(request, 'pos/main/bill_print.html', context)


@login_required(login_url='/pos/login')
def search_supplier(request):
    supno = Supplier.objects.all()
    serializer = SupplierSerializer(supno, many=True)
    context = {
        'supno': serializer.data
    }
    return render(request, 'pos/main/search_supplier.html', context)

import random
import string

def generate_unique_sale_number():
    random_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    random_digits = ''.join(random.choice(string.digits) for _ in range(3))
    pnr_number = f'{random_letters}{random_digits}'
    return pnr_number


@login_required(login_url='/pos/login')
def search_barcode(request):
    return render(request, 'pos/main/search_barcode.html')    

@login_required(login_url='/pos/login')
def update_price(request):
    return render(request, 'pos/main/update_price.html') 

@login_required(login_url='/pos/login')
def take_pic(request):
    return render(request, 'pos/main/take_pic.html') 

# added by sarvesh - 27-12-23
from django.db.models import Sum
from django.views import View
from django.db.models.functions import ExtractMonth

class AnalysisView(View):

    @login_required(login_url='/pos/login')
    def analysis(request):
        return render(request, 'pos/main/analysis.html')
    
    # item wise - starts here:
    @login_required(login_url='/pos/login')
    def itemWise(request):
    # Fetch relevant data for item-wise analysis
        item_data = Sale.objects.annotate(month=ExtractMonth('salenumber__salesCreatedDate')).values('headline', 'month').annotate(total_qty=Sum('rowTotal'))

        # Prepare data for Chart.js
        datasets = []
        unique_titles = set(item['headline'] for item in item_data)
        for title in unique_titles:
            title_data = [item['total_qty'] if item['headline'] == title else 0 for item in item_data]
            datasets.append({'label': title, 'data': title_data})

        # Prepare data for the responsive table
        table_data = [{'title': item['headline'], 'qty': item['total_qty'], 'month': item['month']} for item in item_data]
        context = {
            'datasets': datasets,
            'labels': ['Jan','Feb','March','April','May'],  
            'table_data': table_data,
        }
        return render(request, 'pos/analysis/itemwise.html', context)

    
    @login_required(login_url='/pos/login')
    def itemWiseData(request,item):
        graph_data = Sale.objects.filter(headline=item).values('salenumber__storeName').annotate(total=Sum('rowTotal'))                
        item_data = Sale.objects.filter(headline=item).values('salenumber__saleNumber','salenumber__storeName').annotate(total=Sum('rowTotal'))                
        table_data = [{'saleNo': item['salenumber__saleNumber'], 'storeName': item['salenumber__storeName'],'total':item['total']} for item in item_data]
        context = {            
            'table_data': table_data,
            'labels':[item['salenumber__storeName'] for item in graph_data],
            'data':[item['total'] for item in graph_data]
        }

        return render(request, 'pos/analysis/itemwisedata.html',context)

    # item wise - ends here
    @login_required(login_url='/pos/login')
    def priceWise(request):
        price_data = Sale.objects.annotate(month=ExtractMonth('salenumber__salesCreatedDate')).values('rowRate', 'month').annotate(total_qty=Sum('rowQty'))
        datasets = []
        unique_prices = set(item['rowRate'] for item in price_data)
        for price in unique_prices:
            price_data_filtered = [item['total_qty'] if isinstance(item, dict) and item.get('rowRate') == price else 0 for item in price_data]
            datasets.append({'label': price, 'data': price_data_filtered})

        table_data = [{'price': item.get('rowRate', 0), 'qty': item.get('total_qty', 0), 'month': item.get('month', 0)} for item in price_data if isinstance(item, dict)]
        
        context = {
            'datasets': datasets,
            'labels': ['Jan', 'Feb', 'March', 'April', 'May'],
            'table_data': table_data,
            'price_data': price_data,
        }
        return render(request, 'pos/analysis/pricewise.html', context)

    @login_required(login_url='/pos/login')
    def supplierWise(request):
        supplier_data = Sale.objects.values('supplier').annotate(month=ExtractMonth('salenumber__salesCreatedDate')).values('supplier', 'month').annotate(total_qty=Sum('rowQty'))
        datasets = []
        unique_suppliers = set(item['supplier'] for item in supplier_data)
        
        for supplier in unique_suppliers:
            supplier_data_filtered = [item['total_qty'] if isinstance(item, dict) and item.get('supplier') == supplier else 0 for item in supplier_data]
            datasets.append({'label': supplier, 'data': supplier_data_filtered})

        table_data = [{'supplier': item.get('supplier', 0), 'qty': item.get('total_qty', 0), 'month': item.get('month', 0)} for item in supplier_data if isinstance(item, dict)]
        
        context = {
            'datasets': datasets,
            'labels': ['Jan', 'Feb', 'March', 'April', 'May'],  
            'table_data': table_data,
            'supplier_data': supplier_data,
        }
        return render(request, 'pos/analysis/supplierwise.html', context)

    @login_required(login_url='/pos/login')
    def cityWise(request):
        return render(request, 'pos/analysis/citywise.html')
    
    @login_required(login_url='/pos/login')
    def viewMasterInput(request):
        return render(request, 'pos/analysis/viewmasterinput.html')
    

def handle_scanned_data(request):
    scanned_data = request.GET.get('scanned_data')
    # Process the scanned data as needed
    
    return JsonResponse({'status': 'success'})

    
    


