# Generated by Django 3.2.7 on 2023-09-13 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20230723_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch_data',
            name='Bill_no',
            field=models.CharField(blank=True, db_index=True, default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='Inward_no',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 13, 11, 1, 24, 636209)),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='packed_quantity',
            field=models.FloatField(blank=True, db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='supplier',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 13, 11, 1, 24, 636209)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 13, 11, 1, 24, 636209)),
        ),
    ]
