# Generated by Django 3.2.7 on 2023-12-19 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_auto_20231219_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsup', models.BooleanField(default=False, verbose_name='')),
                ('main_name', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('name', models.CharField(max_length=120)),
                ('supplier_code', models.CharField(blank=True, default='', max_length=20)),
                ('area', models.CharField(blank=True, default='', max_length=30)),
                ('address_line_1', models.CharField(blank=True, default='', max_length=120)),
                ('address_line_2', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('state', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.CharField(blank=True, default='', max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('email1', models.EmailField(blank=True, default='', max_length=50, null=True)),
                ('mobile_no_1', models.CharField(blank=True, max_length=20)),
                ('mobile_no_2', models.CharField(blank=True, max_length=20, null=True)),
                ('name1', models.CharField(blank=True, default='', max_length=120)),
                ('name2', models.CharField(blank=True, default='', max_length=120)),
                ('gst_no', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('pan', models.CharField(blank=True, default='', max_length=10)),
                ('bank', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('branch', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Account_No', models.CharField(blank=True, max_length=20, null=True)),
                ('ifsc_code', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('remarks', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('sup_created_date', models.DateTimeField(default=datetime.datetime(2023, 12, 19, 23, 34, 10, 16289))),
            ],
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 23, 34, 10, 13734)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 23, 34, 10, 14262)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 23, 34, 10, 15287)),
        ),
    ]
