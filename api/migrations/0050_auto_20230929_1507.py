# Generated by Django 2.2.28 on 2023-09-29 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_auto_20230929_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 15, 7, 55, 22383)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 15, 7, 55, 22383)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 15, 7, 55, 22383)),
        ),
    ]
