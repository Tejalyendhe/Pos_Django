# Generated by Django 5.0.1 on 2024-01-23 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0081_alter_dispatch_data_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='supplier_name',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 16, 29, 14, 222119)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 16, 29, 14, 222119)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 16, 29, 14, 222119)),
        ),
    ]
