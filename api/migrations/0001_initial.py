# Generated by Django 3.2.11 on 2022-07-02 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dispatch_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Inward_no', models.CharField(default='', max_length=40)),
                ('Unique_no', models.CharField(blank=True, default='', max_length=40)),
                ('Product_name', models.CharField(default='', max_length=40)),
                ('supplier', models.CharField(default='', max_length=40)),
                ('Color', models.CharField(blank=True, default='', max_length=40)),
                ('Qty', models.FloatField(blank=True, default=1)),
                ('Height', models.FloatField(blank=True, default=0)),
                ('Width', models.FloatField(blank=True, default=0)),
                ('Depth', models.FloatField(blank=True, default=0)),
                ('Size', models.CharField(blank=True, default='', max_length=15)),
                ('Headline', models.CharField(blank=True, default='', max_length=60)),
                ('Description', models.TextField(blank=True, default='')),
                ('Description_2', models.TextField(blank=True, default='')),
                ('Sup_sl_np', models.CharField(blank=True, default='', max_length=5)),
                ('Material', models.CharField(blank=True, default='', max_length=40)),
                ('Finish', models.CharField(blank=True, default='', max_length=40)),
                ('Type', models.CharField(blank=True, default='', max_length=40)),
                ('Photo_link', models.CharField(blank=True, default='', max_length=5000)),
                ('Photo_link_main', models.CharField(blank=True, default='', max_length=300)),
                ('Rate', models.FloatField(blank=True, default=0)),
                ('Calculation', models.CharField(blank=True, default='', max_length=60)),
                ('Cipher', models.CharField(blank=True, default='', max_length=60)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 7, 2, 17, 37, 25, 702938))),
                ('add1', models.FloatField(blank=True, default=0)),
                ('add2', models.FloatField(blank=True, default=0)),
                ('add1a', models.FloatField(blank=True, default=0)),
                ('add2a', models.FloatField(blank=True, default=0)),
                ('Bill_no', models.CharField(blank=True, default='', max_length=60)),
                ('greturn', models.FloatField(blank=True, default=0)),
                ('Packing_no', models.CharField(default='', max_length=10)),
                ('packed_quantity', models.FloatField(blank=True, default=0)),
                ('Carton_No', models.CharField(blank=True, max_length=10)),
                ('Invoice_No', models.CharField(blank=True, default='', max_length=20)),
                ('Transport_By', models.CharField(blank=True, choices=[('air', 'AIR'), ('sea', 'SEA'), ('land', 'LAND'), ('other', 'OTHER')], max_length=15)),
                ('distpatch_no', models.CharField(blank=True, max_length=11)),
            ],
        ),
    ]
