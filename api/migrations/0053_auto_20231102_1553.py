# Generated by Django 2.2.28 on 2023-11-02 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_auto_20231010_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 15, 53, 26, 825322)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 15, 53, 26, 827317)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 15, 53, 26, 828314)),
        ),
    ]
