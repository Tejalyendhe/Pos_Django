# Generated by Django 2.2.28 on 2023-12-26 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_auto_20231226_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 41, 48, 408263)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 41, 48, 410257)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 41, 48, 411283)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 41, 48, 414274)),
        ),
    ]
