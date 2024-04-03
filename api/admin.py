from django.contrib import admin
from .models import Dispatch_data,DispacthPostUser, DispatchNumber,MacidData,StoreType,SaleData,Sale,UpdatedPrice,StaticBarcode,Trigger,Supplier,UserType
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


admin.site.register(Dispatch_data)
admin.site.register(DispacthPostUser)
admin.site.register(MacidData)
admin.site.register(StoreType)
admin.site.register(DispatchNumber)
# admin.site.register(SaleData)
admin.site.register(Sale)
admin.site.register(UpdatedPrice) # added on 27-12-22
admin.site.register(Trigger) # added on 23-07-23
admin.site.register(Supplier) # added on 19-12- 23

class SaleAdmin(admin.TabularInline):
    model = Sale


@admin.register(SaleData)
class SaleDataAdmin(admin.ModelAdmin):
    inlines=[SaleAdmin,]

# added on 29th May 23 by sarvesh


class StaticBarcodeAdmin(admin.ModelAdmin):
    readonly_fields = ('dispatch_no', 'inward_no')

admin.site.register(StaticBarcode, StaticBarcodeAdmin)

class CustomUserTypeInline(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = "UserType"

class CustomizedUserAdmin (UserAdmin):
    inlines = (CustomUserTypeInline,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(UserType)