# Generated by Django 3.2.7 on 2023-12-29 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_auto_20231228_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 13, 43, 1, 847630)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 13, 43, 1, 847630)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 13, 43, 1, 847630)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 13, 43, 1, 847630)),
        ),
    ]
