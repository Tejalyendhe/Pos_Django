# Generated by Django 3.2.7 on 2022-10-13 18:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20221008_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saledata',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='saledata',
            name='rowQty',
        ),
        migrations.RemoveField(
            model_name='saledata',
            name='rowRate',
        ),
        migrations.RemoveField(
            model_name='saledata',
            name='rowTotal',
        ),
        migrations.RemoveField(
            model_name='saledata',
            name='uniqueNumber',
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 23, 42, 45, 688372)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 23, 42, 45, 690366)),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='saleNumber',
            field=models.CharField(blank=True, default='', max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 23, 42, 45, 690366)),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueNumber', models.CharField(blank=True, default='', max_length=8)),
                ('headline', models.CharField(blank=True, default='', max_length=18)),
                ('rowQty', models.CharField(blank=True, default='', max_length=20)),
                ('rowTotal', models.CharField(blank=True, default='', max_length=20)),
                ('rowRate', models.CharField(blank=True, default='', max_length=20)),
                ('salenumber', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.saledata', to_field='saleNumber')),
            ],
        ),
    ]
