# Generated by Django 5.0.1 on 2024-02-01 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0085_saledata_supplier_alter_dispatch_data_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='supplier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 15, 35, 23, 325448)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 15, 35, 23, 325448)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 15, 35, 23, 325448)),
        ),
    ]
