# Generated by Django 3.2.7 on 2022-10-08 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20220927_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledata',
            name='headline',
            field=models.CharField(blank=True, default='', max_length=18),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 8, 21, 5, 51, 658166)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 8, 21, 5, 51, 661289)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 8, 21, 5, 51, 662366)),
        ),
    ]
