# Generated by Django 3.2.7 on 2023-12-29 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0061_auto_20231229_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 20, 57, 19, 381682)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 20, 57, 19, 381682)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 20, 57, 19, 381682)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 20, 57, 19, 381682)),
        ),
    ]
