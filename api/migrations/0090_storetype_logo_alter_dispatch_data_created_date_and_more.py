# Generated by Django 5.0.1 on 2024-02-02 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0089_alter_dispatch_data_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='storetype',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='store_logos/'),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 15, 41, 53, 760556)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 15, 41, 53, 760556)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 15, 41, 53, 760556)),
        ),
    ]
