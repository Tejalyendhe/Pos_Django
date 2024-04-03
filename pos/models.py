from django.db import models

# Create your models here.
class ItemWithoutLabel(models.Model):
    item = models.CharField(max_length=50,default='',blank=True)
    code = models.CharField(max_length=10,default='',blank=True)
    default_rate = models.FloatField(default=0,blank=True)
    default_qty = models.IntegerField(default=1,blank=True)
    supplier = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'{self.item}'
    
# added by sarvesh 05-01-23
class BillDiscount(models.Model):
    position = models.IntegerField(blank=True,default = 0)
    discount_name = models.CharField(max_length=10,default='',blank=True)
    discount_value = models.CharField(max_length=4,default='',blank=True)
    discount_icon = models.CharField(max_length=500,default='',blank=True)
    def __str__(self):
        return f'{self.discount_name}'