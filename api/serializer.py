from rest_framework import serializers

from .models import DispacthPostUser, Dispatch_data, Sale, SaleData, Supplier, UpdatedPrice


class dispatchSerializer(serializers.ModelSerializer):
    distpatch_no = serializers.CharField(source='distpatch_no.distpatch_no')
    class Meta:
        model = Dispatch_data
        fields = '__all__'

class dispatchNumberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dispatch_data
        fields = '__all__'

class DispacthPostUserSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='store.store')
    class Meta:
        model = DispacthPostUser
        fields = ['username','password','store','user_type']

import json

from django.core import serializers as core_serializers


class SaleDataSerializer(serializers.ModelSerializer):
    sale = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = SaleData
        fields = '__all__'

    def get_sale(self,saledata):
        sale_data =Sale.objects.filter(salenumber=saledata.saleNumber).only('uniqueNumber','headline','rowQty','rowTotal','rowRate')
        data = json.loads(core_serializers.serialize('json',sale_data))
        return data
    
# added on 27-12-22
class UpdatedPriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UpdatedPrice
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'