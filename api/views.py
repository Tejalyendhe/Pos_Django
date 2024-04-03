
import json
from datetime import datetime

import requests
from api.models import (DispacthPostUser, Dispatch_data, DispatchNumber,
                        MacidData, Sale, SaleData, StoreType, User_type,UpdatedPrice,Trigger,Supplier)
from django.http import HttpResponse, JsonResponse
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import (DispacthPostUserSerializer, SaleDataSerializer, SupplierSerializer,
                         dispatchSerializer, dispatchNumberSerializer,UpdatedPriceSerializer)


@api_view(['GET'])
def dispatch_data(request,dn,un,up):
    # Dispatch_data.objects.all().delete()
    dis_data = Dispatch_data.objects.filter(distpatch_no=dn)
    serializer = dispatchSerializer(dis_data,many=True)

    return Response(serializer.data)

@csrf_exempt
def add_dispatch_data(request):
    if request.method == "POST":
        response_data ={}

        user = request.POST['user']
        if user in DispacthPostUser.objects.values_list('username',flat=True):
            for i in (json.loads(request.POST['product_data'])):
                unique_num  = i['product']['Unique_no']
                inward_no = i['product']['Inward_no']
                product_name = i['product']['Product_name']
                supplier = i['product']['supplier']
                color = i['product']['Color']
                qty = i['product']['Qty']
                height = i['product']['Height']
                width = i['product']['Width']
                depth = i['product']['Depth']
                size = i['product']['Size']
                headline = i['product']['Headline']
                description = i['product']['Description']
                description_2 = i['product']['Description_2']
                sup_sl_np = i['product']['Sup_sl_np']
                material = i['product']['Material']
                finish = i['product']['Finish']
                type = i['product']['Type']
                photo_link = i['product']['Photo_link']
                photo_link_main = i['product']['Photo_link_main']
                rate = i['product']['Rate']
                calculation = i['product']['Calculation']
                cipher = i['product']['Cipher']
                created_date = i['product']['created_date']
                add1 = i['product']['add1']
                add2 = i['product']['add2']
                add1a = i['product']['add1a']
                add2a = i['product']['add2a']
                bill_no = i['product']['Bill_no']
                greturn = i['product']['greturn']
                label_qty = i['product']['Label_qty']
                packed_qty = i['Quantity']
                invoice_no = i['Invoice_no']
                packing_no = i['Packing_no']
                carton_No = i['carton_data']['Carton_No']
                transport_By = i['carton_data']['Transport_By']
                disp_numb = i['carton_data']['disp_numb']
                if unique_num=='' or unique_num == ' ' or unique_num == None:
                    pass

                if disp_numb not in DispatchNumber.objects.values_list('distpatch_no',flat=True):
                    DispatchNumber.objects.create(distpatch_no=disp_numb,store = StoreType.objects.get(store="CELEBRATIONS"), status= True)

                disp_numb=DispatchNumber.objects.get(distpatch_no=disp_numb)
                
                     
                if unique_num in Dispatch_data.objects.values_list('Unique_no',flat=True):
                    disp = Dispatch_data.objects.get(Unique_no=unique_num)
                    disp.Inward_no=inward_no
                    disp.Product_name=product_name
                    disp.supplier=supplier
                    disp.Color=color
                    disp.Qty=qty
                    disp.Height=height
                    disp.Width=width
                    disp.Depth=depth
                    disp.Size=size
                    disp.Headline=headline
                    disp.Description=description
                    disp.Description_2=description_2
                    disp.Sup_sl_np=sup_sl_np
                    disp.Material=material 
                    disp.Finish=finish
                    disp.Type=type
                    disp.Photo_link=photo_link
                    disp.Photo_link_main=photo_link_main
                    disp.Rate=rate
                    disp.Calculation=calculation 
                    disp.Cipher=cipher
                    disp.created_date=created_date
                    disp.add1=add1
                    disp.add2=add2
                    disp.add1a=add1a
                    disp.add2a=add2a
                    disp.Bill_no=bill_no
                    disp.greturn=greturn 
                    disp.Label_qty=label_qty
                    disp.packed_quantity+=float(packed_qty) 
                    disp.Invoice_No=invoice_no 
                    disp.Packing_no=f'{disp.Packing_no} , {packing_no}'
                    disp.Carton_No=carton_No
                    disp.Transport_By=transport_By
                    disp.distpatch_no=disp_numb
                    disp.save()
                else:
                    Dispatch_data.objects.create(
                        Unique_no=unique_num,Inward_no=inward_no,Product_name=product_name,supplier=supplier,Color=color,Qty=qty,
                        Height=height,Width=width,Depth=depth,Size=size,Headline=headline,Description=description,Description_2=description_2,
                        Sup_sl_np=sup_sl_np,Material=material,Finish=finish,Type=type,Photo_link=photo_link,Photo_link_main=photo_link_main,
                        Rate=rate,Calculation=calculation,Cipher=cipher,created_date=created_date,
                        add1=add1,add2=add2,add1a=add1a,add2a=add2a,Bill_no=bill_no,
                        greturn=greturn,Label_qty=label_qty,packed_quantity=packed_qty,Invoice_No=invoice_no,Packing_no=packing_no,
                        Carton_No=carton_No,Transport_By=transport_By,distpatch_no=disp_numb
                    )

            



    response_data['message'] = 'save successfully'
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_dispatch_data(request):
    if request.method == "GET":
        req = json.loads(request.body)
        data={}
        if Trigger.objects.get(name='MacId').trigger == True:
            mac_id = req['mac_id']
            if mac_id in MacidData.objects.values_list('mac_id',flat=True):
                disp_no = req['dispatch_no']
                if disp_no in Dispatch_data.objects.values_list('distpatch_no__distpatch_no',flat=True):

                    dis_data = Dispatch_data.objects.filter(distpatch_no__distpatch_no=disp_no)
                    serializer = dispatchSerializer(dis_data,many=True)
                    data['product_data']=json.dumps((serializer.data))
                    return JsonResponse(data, content_type="application/json")
                else:
                    data['product_data']='No Dispatch Found'
                    return JsonResponse(data, content_type="application/json")
            else:
                data['product_data'] = 'ERROR 403 FORBIDDEN'
                return JsonResponse(data, content_type="application/json")
        else:
            disp_no = req['dispatch_no']
            if disp_no in Dispatch_data.objects.values_list('distpatch_no__distpatch_no',flat=True):

                dis_data = Dispatch_data.objects.filter(distpatch_no__distpatch_no=disp_no)
                serializer = dispatchSerializer(dis_data,many=True)
                data['product_data']=json.dumps((serializer.data))
                return JsonResponse(data, content_type="application/json")
            else:
                data['product_data']='No Dispatch Found'
                return JsonResponse(data, content_type="application/json")

#user apis
@csrf_exempt
def create_new_user(request):
    data={}
    if request.method == "POST":
        req = json.loads(request.body)
        if Trigger.objects.get(name='MacId').trigger == True:
            mac_id = req['mac_id']
            if mac_id in MacidData.objects.values_list('mac_id',flat=True):
                app_username = req['applier_username']
                app_password = req['applier_password']
                username = req['username']
                password = req['password']
                store = req['store']
                store = StoreType.objects.filter(store=store)[0]
                user_type = req['user_type']
                if app_username in DispacthPostUser.objects.values_list('username',flat=True):
                    user = DispacthPostUser.objects.filter(username=app_username)[0]
                    if user.password == app_password and user.user_type =="ADMIN":
                        if username not in DispacthPostUser.objects.values_list('username',flat=True):
                            DispacthPostUser.objects.create(username=username,password=password,store=store,user_type=user_type)
                            data['User_Data'] = 'Success'
                        else:
                            data['User_Data'] = 'User Already Exist'
                    else:
                        data['User_Data'] = "You donot have the necessary permissions"
                else:
                    data['User_Data'] = "You donot have the necessary permissions"
                return JsonResponse(data, content_type="application/json")
            else:
                data['User_Data'] = 'ERROR 403 FORBIDDEN'
                return JsonResponse(data, content_type="application/json")
        else:
            app_username = req['applier_username']
            app_password = req['applier_password']
            username = req['username']
            password = req['password']
            store = req['store']
            store = StoreType.objects.filter(store=store)[0]
            user_type = req['user_type']
            if app_username in DispacthPostUser.objects.values_list('username',flat=True):
                user = DispacthPostUser.objects.filter(username=app_username)[0]
                if user.password == app_password and user.user_type =="ADMIN":
                    if username not in DispacthPostUser.objects.values_list('username',flat=True):
                        DispacthPostUser.objects.create(username=username,password=password,store=store,user_type=user_type)
                        data['User_Data'] = 'Success'
                    else:
                        data['User_Data'] = 'User Already Exist'
                else:
                    data['User_Data'] = "You donot have the necessary permissions"
            else:
                data['User_Data'] = "You donot have the necessary permissions"
            return JsonResponse(data, content_type="application/json")


def get_user_byStore(request):
    data = {}
    if request.method == "GET":
        req = json.loads(request.body)
        if Trigger.objects.get(name='MacId').trigger == True:
            mac_id = req['mac_id']
            if mac_id in MacidData.objects.values_list('mac_id',flat=True):
                store = req['store']
                app_username = req['applier_username']
                app_password = req['applier_password']
                if app_username in DispacthPostUser.objects.values_list('username',flat=True):
                    user = DispacthPostUser.objects.filter(username=app_username)[0]
                    if user.password == app_password and user.user_type =="ADMIN":
                        store = StoreType.objects.filter(store=store)[0]
                        user_data = DispacthPostUser.objects.filter(store=store)
                        serializer = DispacthPostUserSerializer(user_data,many=True)
                        data['user_data']=json.dumps((serializer.data))             
                    else:
                        data['User_Data'] = "You donot have the necessary permissions"
                else:
                    data['User_Data'] = "You donot have the necessary permissions"
                return JsonResponse(data, content_type="application/json")
            else:
                data['User_Data'] = 'ERROR 403 FORBIDDEN'
                return JsonResponse(data, content_type="application/json")
        else:
            store = req['store']
            app_username = req['applier_username']
            app_password = req['applier_password']
            print(app_password,app_username)
            if app_username in DispacthPostUser.objects.values_list('username',flat=True):
                user = DispacthPostUser.objects.filter(username=app_username)[0]
                if user.password == app_password and user.user_type =="ADMIN":
                    store = StoreType.objects.filter(store=store)[0]
                    user_data = DispacthPostUser.objects.filter(store=store)
                    serializer = DispacthPostUserSerializer(user_data,many=True)
                    data['user_data']=json.dumps((serializer.data))             
                else:
                    data['User_Data'] = "You donot have the necessary permissions"
            else:
                data['User_Data'] = "You donot have the necessary permissions"
            return JsonResponse(data, content_type="application/json")

@csrf_exempt
def delete_user(request):
    data = {}
    if request.method == "DELETE":
        req = json.loads(request.body)
        if Trigger.objects.get(name='MacId').trigger == True:
            mac_id = req['mac_id']
            if mac_id in MacidData.objects.values_list('mac_id',flat=True):
                username = req['applier_username']
                password = req['applier_password']
                deluser = req['username']
                if username in DispacthPostUser.objects.values_list('username',flat=True):
                    user = DispacthPostUser.objects.filter(username=username)[0]
                    if user.password == password and user.user_type =="ADMIN":
                        if deluser in DispacthPostUser.objects.values_list('username',flat=True):
                            user = DispacthPostUser.objects.filter(username=deluser)
                            user.delete();
                            data['User_Data'] = "Sucessfully deleted user"   
                        else:
                            data['User_Data'] = "User doesnot exist"    
                    else:
                        data['User_Data'] = "You donot have the necessary permissions"
                else:
                    data['User_Data'] = "You donot have the necessary permissions"
            else:
                data['User_Data'] = 'ERROR 403 FORBIDDEN'
            return JsonResponse(data, content_type="application/json")
        else:
            username = req['applier_username']
            password = req['applier_password']
            deluser = req['username']
            if username in DispacthPostUser.objects.values_list('username',flat=True):
                user = DispacthPostUser.objects.filter(username=username)[0]
                if user.password == password and user.user_type =="ADMIN":
                    if deluser in DispacthPostUser.objects.values_list('username',flat=True):
                        user = DispacthPostUser.objects.filter(username=deluser)
                        user.delete();
                        data['User_Data'] = "Sucessfully deleted user"   
                    else:
                        data['User_Data'] = "User doesnot exist"    
                else:
                    data['User_Data'] = "You donot have the necessary permissions"
            else:
                data['User_Data'] = "You donot have the necessary permissions"

def get_dispatch_numbers(request):
    data = {}
    if request.method == "GET":
        req = json.loads(request.body)
        if Trigger.objects.get(name='MacId').trigger == True:
            mac_id = req['mac_id']
            if mac_id in MacidData.objects.values_list('mac_id',flat=True):
                store = req['store']
                store = StoreType.objects.filter(store=store)[0]
                dis_data = DispatchNumber.objects.filter(store=store,status=True)
                serializer = dispatchNumberSerializer(dis_data,many=True)
                data['dispatch_numbers']=json.dumps((serializer.data))
                return JsonResponse(data, content_type="application/json")
            else:
                data['dispatch_numbers'] = 'ERROR 403 FORBIDDEN'
                return JsonResponse(data, content_type="application/json")
        else:   
            store = req['store']
            store = StoreType.objects.filter(store=store)[0]
            dis_data = DispatchNumber.objects.filter(store=store,status=True)
            serializer = dispatchNumberSerializer(dis_data,many=True)
            data['dispatch_numbers']=json.dumps((serializer.data))
            return JsonResponse(data, content_type="application/json")

@csrf_exempt
def push_sales_data(request):
    if request.method=='POST':
        req = json.loads(request.body)
        data={}
        count=0
        for i in req['product_data']:
           saleNumber = i['saleNumber'] 
           storeName = i['storeName'] 
           salesCreatedDate = datetime.strptime(i['salesCreatedDate'], "%Y-%m-%d %H:%M:%S") 
           saleTotal = i['saleTotal'] 
           saleDiscount = i['saleDiscount'] 
           saleCard = i['saleCard'] 
           saleCash = i['saleCash'] 
           salePoints = i['salePoints'] 
           saleBalance = i['saleBalance'] 
           saledata=i['data']
           isNotExchange=i['isNotExchange']
           if saleNumber not in SaleData.objects.values_list('saleNumber',flat=True):
            sale = SaleData.objects.create(saleNumber=saleNumber,storeName=storeName,salesCreatedDate=salesCreatedDate,
            saleTotal=saleTotal,saleDiscount=saleDiscount,saleCard=saleCard,saleCash=saleCash,salePoints=salePoints,
            saleBalance=saleBalance,isNotExchange=isNotExchange) 
            for i in saledata:
                salerow = i.split(',')
                try:
                    uniqueNumber = salerow[0]
                    headline = salerow[1]
                    rowQty = salerow[2]
                    rowRate = salerow[3]
                    rowTotal = salerow[4]
                    Sale.objects.create(salenumber=sale,uniqueNumber=uniqueNumber,headline=headline,rowQty=rowQty,rowTotal=rowTotal,rowRate=rowRate)
                except Exception as e:
                    pass
            count+=1
        if count > 1:
            data['response_message'] = f'{count} products has been pushed successfully.'
            return JsonResponse(data, content_type="application/json")
        elif count == 1:
            data['response_message'] = f'{count} product has been pushed successfully.'
            return JsonResponse(data, content_type="application/json")
        else:
            data['response_message'] = f'Already upto date.'
            return JsonResponse(data, content_type="application/json")  

def get_sales_data(request):
    if request.method == "GET":
        req = json.loads(request.body)
        req_filter = req['req_filter']
        req_value = req['req_value']
        req_user = req['user']
        data={}
        if req_filter == 'store_name':
            sale_data = SaleData.objects.filter(storeName__contains=req_value)
            serializer = SaleDataSerializer(sale_data,many=True)
            data['response_data']=json.dumps((serializer.data))
            return JsonResponse(data, content_type="application/json")
        elif req_filter == 'headline':
            sale_data = SaleData.objects.filter(headline__contains=req_value)
            serializer = SaleDataSerializer(sale_data,many=True)
            data['response_data']=json.dumps((serializer.data))
            return JsonResponse(data, content_type="application/json")
        elif req_filter == 'saleNumber':
            sale_data = SaleData.objects.filter(saleNumber__contains=req_value)
            serializer = SaleDataSerializer(sale_data,many=True)
            data['response_data']=json.dumps((serializer.data))
            return JsonResponse(data, content_type="application/json")
        elif req_filter == 'unique_number':
            sale_data = SaleData.objects.filter(uniqueNumber__contains=req_value)
            serializer = SaleDataSerializer(sale_data,many=True)
            data['response_data']=json.dumps((serializer.data))
            return JsonResponse(data, content_type="application/json")


@api_view(['GET'])
def get_sales_data(request,sn):

    sale_data = SaleData.objects.filter(saleNumber__contains=sn)
    serializer = SaleDataSerializer(sale_data,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_user_data(request):

    user_data = DispacthPostUser.objects.all()
    serializer = DispacthPostUserSerializer(user_data,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fetch_by_barcode(request):
    data ={}
    if request.method == "GET":
            req = json.loads(request.body)
            if Trigger.objects.get(name='MacId').trigger == True:
                mac_id = req['mac_id']
                if mac_id in MacidData.objects.values_list('mac_id',flat=True):
                    barcode = req['barcode']                
                    if barcode in Dispatch_data.objects.values_list('Unique_no',flat=True):
                        product = Dispatch_data.objects.filter(Unique_no=barcode)                    
                        serializer = dispatchSerializer(product,many=True)
                        data['Product_Data']=json.dumps((serializer.data))                                 
                    else:
                        data['Product_Data'] = "Barcode Not Found."
                    return JsonResponse(data, content_type="application/json")
                else:
                    data['Product_Data'] = 'ERROR 403 FORBIDDEN.'
                    return JsonResponse(data, content_type="application/json")
            else:
                barcode = req['barcode']                
                if barcode in Dispatch_data.objects.values_list('Unique_no',flat=True):
                    product = Dispatch_data.objects.filter(Unique_no=barcode)                    
                    serializer = dispatchSerializer(product,many=True)
                    data['Product_Data']=json.dumps((serializer.data))                                 
                else:
                    data['Product_Data'] = "Barcode Not Found."
                return JsonResponse(data, content_type="application/json")


# added on 27-12-22
@csrf_exempt
def save_updated_price(request):
    if request.method=='POST':
        print(json.loads(request.body))
        req = json.loads(request.body)
        data={}
        count=1
        if Trigger.objects.get(name='MacId').trigger == True:
            mac_id = req['mac_id']
            if mac_id not in MacidData.objects.values_list('mac_id',flat=True):
                data['message'] = 'ERROR !!! - Mac Id Not Found.'
                return JsonResponse(data, content_type="application/json")
        else:
            pass
        error_data = 'Error while saving: '
        for i in req['products']:
           uniqueNumber = i['uniqueNumber'] 
           headline = i['headline'] 
           updatedPrice = i['updatedPrice'] 
           count=1
           if uniqueNumber in Dispatch_data.objects.values_list('Unique_no',flat=True):
               if uniqueNumber in UpdatedPrice.objects.values_list('uniqueNumber', flat=True):
                   for up in UpdatedPrice.objects.filter(uniqueNumber=uniqueNumber):
                    up.updatedPrice = updatedPrice
                    up.headline = headline
                    up.save()
                   count+=1
               else:
                   UpdatedPrice.objects.create(uniqueNumber=uniqueNumber,updatedPrice=updatedPrice
                   ,headline=headline)
                   count+=1
           else:
               error_data += f''' {i['uniqueNumber']},'''
               pass
        if error_data != 'Error while saving: ' and count>=1:
            data['message'] = f'{count} product has been saved and {error_data}'
            return JsonResponse(data, content_type="application/json")
        elif error_data == 'Error while saving: ' and count>=1:
            data['message'] = f'{count} product has been saved'
            return JsonResponse(data, content_type="application/json")
        else:
           data['message'] = f'Error while saving the products'
           return JsonResponse(data, content_type="application/json")


# added on 27-12-22
def get_updated_price(request):
    data ={}
    if request.method == "GET":
        req = json.loads(request.body)
        uniqueNumber = req['uniqueNumber']
        if Trigger.objects.get(name='MacId').trigger == True:
            mac_id = req['mac_id']
            if mac_id in MacidData.objects.values_list('mac_id',flat=True):
                uniqueNumber = req['uniqueNumber']                
                if   uniqueNumber=='':
                    product = UpdatedPrice.objects.all()                
                    serializer = UpdatedPriceSerializer(product,many=True)
                    data['Product_Data']=json.dumps((serializer.data))  
                elif  uniqueNumber!='' and UpdatedPrice.objects.filter(uniqueNumber=uniqueNumber).exists:  
                    product = UpdatedPrice.objects.filter(uniqueNumber=uniqueNumber)  
                    serializer = UpdatedPriceSerializer(product,many=True)
                    data['Product_Data']=json.dumps((serializer.data))                              
                else:
                    data['Product_Data'] = "Data Not Found."
                return JsonResponse(data, content_type="application/json")
            else:
                data['Product_Data'] = 'ERROR 403 FORBIDDEN.'
                return JsonResponse(data, content_type="application/json")
        else:
            uniqueNumber = req['uniqueNumber']                
            if uniqueNumber=='':
                product = UpdatedPrice.objects.all()                
                serializer = UpdatedPriceSerializer(product,many=True)
                data['Product_Data']=json.dumps((serializer.data))  
            elif uniqueNumber!='' and UpdatedPrice.objects.filter(uniqueNumber=uniqueNumber).exists:  
                product = UpdatedPrice.objects.filter(uniqueNumber=uniqueNumber)  
                serializer = UpdatedPriceSerializer(product,many=True)
                data['Product_Data']=json.dumps((serializer.data))                              
            else:
                data['Product_Data'] = "Data Not Found."
            return JsonResponse(data, content_type="application/json")



# added by sarvesh - 19th Dec 23 (Push supplier's data to dispatch server)

@csrf_exempt
def add_supplier_data(request):
    if request.method == "POST":
        response_data ={}
        try:

            user = request.POST['user']
            if user in DispacthPostUser.objects.values_list('username', flat=True):
                for i in json.loads(request.POST['supplier_data']):
                    supplier_code = i['supplier_code']

                    # Use filter to get a queryset of objects with the same supplier_code
                    suppliers = Supplier.objects.filter(supplier_code=supplier_code)

                    if suppliers.exists():
                        # Update each matching object with the provided data
                        for sup in suppliers:
                            for key, value in i.items():
                                setattr(sup, key, value)
                            sup.save()
                    else:
                        # If no matching object exists, create a new one
                        Supplier.objects.create(**i)
            response_data['message'] = 'save successfully'
        except Exception as e:
            print(e)
            response_data['message'] = 'error occured'
        return JsonResponse(response_data)

@api_view(['GET'])
def supplier_api(request):
    try:
        supno = Supplier.objects.all()
        serializer = SupplierSerializer(supno, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
    return Response({'error': 'An error occurred'}, status=500)
    
def checkPost(request):
    
    # data={
    #     'mac_id':'ce5abdf15cd23ee9',
    #     'products':[
    #      {
    #     'uniqueNumber':'11AA5681',
    #     'headline':'Updated SAREE Price',
    #     'updatedPrice':'3000',
    #     },
    #      {
    #     'uniqueNumber':'11AA5694',
    #     'headline':'Updated KURTA Price',
    #     'updatedPrice':'2000',
    #     },
    #     ],

    # }
    
    
    # # product_data = json.dumps(datas)
    # LOGIN_URL = 'http://localhost:5000/save_updated_price'
    # resp = requests.post(LOGIN_URL, data=json.dumps(data),verify=False)
    # rply= resp.json()
    # print(rply['response_message'])
    return HttpResponse(f'''{Trigger.objects.get(name='MacId').trigger}''')
