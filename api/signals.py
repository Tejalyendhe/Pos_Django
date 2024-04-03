from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import StaticBarcode,Dispatch_data,DispatchNumber


@receiver(post_save, sender=StaticBarcode)  # added on 29th May 23 by sarvesh
def StaticBarcodePostSave(sender, instance, created, **kwargs):
    if created:
        disp_no = DispatchNumber.objects.get(distpatch_no = instance.dispatch_no)
        for i in range(1,int(instance.count)+1):
            price = f"{instance.product_initials}{str(i).zfill(8-int(len(instance.product_initials)))}"
            Dispatch_data.objects.create(Inward_no=instance.inward_no,Unique_no=price,Product_name=instance.product_name,Headline =instance.product_name,supplier = disp_no.store.store,Rate=i,distpatch_no=disp_no)
    else:
        pass


@receiver(pre_save, sender=StaticBarcode)
def StaticBarcodePostSave(sender, instance, **kwargs):
    try:
        original_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass  # Object is being created, no need to check for changes
    else:
        # Compare the current product_name with the original value
        if instance.product_name != original_instance.product_name:
            Dispatch_data.objects.filter(Inward_no=instance.inward_no).update(Product_name=instance.product_name)
        if instance.count != original_instance.count:            
            if int(instance.count) > (original_instance.count):
                disp_no = DispatchNumber.objects.get(distpatch_no = instance.dispatch_no)
                for i in range(int(original_instance.count)+1,int(instance.count)+1 ):
                    price = f"{instance.product_initials}{str(i).zfill(8-int(len(instance.product_initials)))}"
                    Dispatch_data.objects.create(Inward_no=instance.inward_no,Unique_no=price,Product_name=instance.product_name,Headline =instance.product_name, supplier = disp_no.store.store,Rate=i,distpatch_no=disp_no)
            elif int(instance.count) < (original_instance.count):
                # can be add in future ...
                pass
            
        
        
