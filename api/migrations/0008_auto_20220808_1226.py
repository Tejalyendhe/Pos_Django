# Generated by Django 3.2.11 on 2022-08-08 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20220808_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispacthpostuser',
            old_name='store_type',
            new_name='store',
        ),
        migrations.RenameField(
            model_name='storetype',
            old_name='store_type',
            new_name='store',
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 8, 12, 26, 16, 230520)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 8, 12, 26, 16, 230520)),
        ),
    ]
