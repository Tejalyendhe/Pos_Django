from django.contrib import admin
from .models import ItemWithoutLabel,BillDiscount
# Register your models here.

admin.site.register(ItemWithoutLabel)
admin.site.register(BillDiscount)