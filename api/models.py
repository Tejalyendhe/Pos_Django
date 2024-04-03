import datetime
from enum import unique
from typing import Tuple
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

Transport_Choices=(
    ('air','AIR'),
    ('sea', 'SEA'),
    ('land','LAND'),
    ('other','OTHER'),

)
User_type=(
    ('ADMIN','ADMIN'),
    ('USER', 'USER'),
    ('SUPERVISIOR', 'SUPERVISIOR'),

)

class StoreType(models.Model):
    store = models.CharField(max_length=50,default='',blank=True)
    def __str__(self):
        return f'{self.store}'

# added by sarvesh - 09-01-24
class UserType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30,choices=User_type,blank=True)
    user_store = models.ManyToManyField(StoreType)
    def __str__(self):
        return f'{self.user}-{self.user_type}' 
    
class DispatchNumber(models.Model):
    distpatch_no = models.CharField(max_length=11,blank=True)
    store = models.ForeignKey( StoreType,default='',blank=True,on_delete=models.SET_NULL,null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.distpatch_no}-{self.store}-{self.status}'
# Create your models here.

class Dispatch_data(models.Model): 
    id=models.AutoField(primary_key=True,blank=True)
    Inward_no=models.CharField(max_length=40,default='',db_index=True) 
    Unique_no=models.CharField(max_length=40,default='',blank=True)
    Product_name = models.CharField(max_length=40,default='')   
    supplier = models.CharField(max_length=40,default='',db_index=True) 
    Color= models.CharField(max_length=40,default='',blank=True)
    Qty=models.FloatField(default=1,blank=True)
    Height=models.FloatField(default=0,blank=True)
    Width=models.FloatField(default=0,blank=True)
    Depth=models.FloatField(default=0,blank=True)
    Size = models.CharField(max_length=15,default='',blank=True ) 
    Headline=models.CharField(max_length=60,default='',blank=True)
    Description=models.TextField(default='',blank=True)
    Description_2=models.TextField(default='',blank=True)
    Sup_sl_np=models.CharField(max_length=5,default='',blank=True)
    Material=models.CharField(max_length=40,default='',blank=True)
    Finish=models.CharField(max_length=40,default='',blank=True)    
    Type=models.CharField(max_length=40,default='',blank=True)
    Photo_link=models.CharField(max_length=5000,default='',blank=True)
    Photo_link_main=models.CharField(max_length=300,default='',blank=True)
    Rate=models.FloatField(default=0,blank=True)
    Calculation=models.CharField(max_length=60,default='',blank=True,)
    Cipher=models.CharField(max_length=60,default='',blank=True)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    add1 = models.FloatField(default=0,blank=True)
    add2 = models.FloatField(default=0,blank=True)
    add1a = models.FloatField(default=0,blank=True)
    add2a = models.FloatField(default=0,blank=True)
    Bill_no=models.CharField(max_length=60,default='',blank=True,db_index=True)
    greturn=models.FloatField(default=0,blank=True)
    Label_qty=models.FloatField(default=1,blank=True)

    Packing_no=models.CharField(max_length=500,default='')
    packed_quantity=models.FloatField(blank=True,default=0,db_index=True)

    Carton_No = models.CharField(max_length=10,blank=True)
    Invoice_No=models.CharField(max_length=20,default='',blank=True)
    Transport_By = models.CharField(max_length=15,choices=Transport_Choices,blank=True)
    # distpatch_no=models.CharField(max_length=20,default='',blank=True)

    distpatch_no = models.ForeignKey(DispatchNumber,default='',blank=True,on_delete=models.CASCADE,null=True)
    Exception_quantity = models.FloatField(default=0,db_index=True)
    def __str__(self):
        return f'{self.Product_name}-{self.Unique_no}-{self.distpatch_no}'

class DispacthPostUser(models.Model):
    username = models.CharField(max_length=40,default='',blank=True)
    password = models.CharField(max_length=300,default='',blank=True)
    store = models.ForeignKey( StoreType,default='',blank=True,on_delete=models.SET_NULL,null=True)
    user_type = models.CharField(max_length=15,choices=User_type,blank=True)
    def __str__(self):
        return f'{self.username}-{self.store}-{self.user_type}'

class MacidData(models.Model):
    mac_id = models.CharField(max_length=75,default='',blank=True)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return f'{self.mac_id}-{self.created_date}'

class SaleData(models.Model):
    user = models.ForeignKey(User,blank=True,on_delete=models.SET_NULL,null=True)
    saleNumber = models.CharField(max_length=18,default='',blank=True,unique=True)
    storeName = models.CharField(max_length=18,default='',blank=True)
    salesCreatedDate = models.DateTimeField(default=timezone.now)
    saleTotal = models.CharField(max_length=20,default='',blank=True)
    saleDiscount = models.CharField(max_length=20,default='',blank=True)
    saleCard = models.CharField(max_length=20,default='',blank=True)
    saleCash = models.CharField(max_length=20,default='',blank=True)
    salePoints = models.CharField(max_length=20,default='',blank=True)
    saleBalance = models.CharField(max_length=20,default='',blank=True)
    isNotExchange= models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return f'{self.storeName}-{self.saleNumber}'

class Sale(models.Model):
    salenumber = models.ForeignKey(SaleData,to_field='saleNumber',default='',blank=True,on_delete=models.SET_NULL,null=True)
    uniqueNumber = models.CharField(max_length=8,default='',blank=True)
    headline = models.CharField(max_length=60,default='',blank=True)
    rowQty = models.CharField(max_length=20,default='',blank=True)
    rowTotal = models.CharField(max_length=20,default='',blank=True)
    rowRate = models.CharField(max_length=20,default='',blank=True)
    supplier = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'{self.salenumber}-{self.uniqueNumber}'

# added on 27-12-22
class UpdatedPrice(models.Model):
    uniqueNumber = models.CharField(max_length=8,default='',blank=True)
    headline = models.CharField(max_length=60,default='',blank=True)
    updatedPrice = models.CharField(max_length=8,default=0,blank=True,null=True)

    def __str__(self):
        return f'{self.uniqueNumber} - {self.headline} - {self.updatedPrice}'
    

# added on 29th May 23 by sarvesh
class StaticBarcode(models.Model):
    # @staticmethod
    def check_inward_no():
        existing_count = StaticBarcode.objects.count()
        return f"ADM{str(existing_count + 1).zfill(6)}"

    dispatch_no = models.CharField(default='DISP1888888',editable=False,max_length=14)
    inward_no = models.CharField(max_length=8, default=check_inward_no, unique=True,editable=False)
    product_name = models.CharField(max_length=30,unique=True)
    product_initials = models.CharField(max_length=5,unique=True)
    count = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.dispatch_no} - {self.inward_no} - {self.product_name}'
    

# added on 23rd July 23 by sarvesh
class Trigger(models.Model):
    name = models.CharField(max_length=14)
    trigger = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name} - {self.trigger}'



# added by sarvesh - 18th Dec 23 (Push supplier's data to dispatch server)
class Supplier(models.Model):
    subsup=models.BooleanField('',default=False)
    main_name=models.CharField(max_length=120,default='',null=True,blank=True)
    name = models.CharField(max_length=120,blank=False)
    supplier_code=models.CharField(max_length=20,default='',blank=True)
    area=models.CharField(max_length=30,default='',blank=True)
    address_line_1=models.CharField(max_length=120,default='',blank=True)
    address_line_2=models.CharField(max_length=50,default='',null=True,blank=True)
    city=models.CharField(max_length=50,default='',blank=True)
    state=models.CharField(max_length=50,default='',blank=True)
    country=models.CharField(max_length=50,default='',blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    email1=models.EmailField(max_length=50,null=True,default='',blank=True)
    mobile_no_1=models.CharField(max_length=20,blank=True)
    mobile_no_2=models.CharField(max_length=20,null=True,blank=True)
    name1 = models.CharField(max_length=120,default='',blank=True)
    name2 = models.CharField(max_length=120,default='',blank=True)
    gst_no=models.CharField(max_length=20,default='',null=True,blank=True)
    pan=models.CharField(max_length=10,default='',blank=True)
    bank=models.CharField(max_length=50,default='',null=True,blank=True)
    branch=models.CharField(max_length=50,default='',null=True,blank=True)
    Account_No=models.CharField(max_length=20,null=True,blank=True,)
    ifsc_code=models.CharField(max_length=20,default='',null=True,blank=True)
    remarks=models.CharField(max_length=120,default='',null=True,blank=True)
    sup_created_date = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.name