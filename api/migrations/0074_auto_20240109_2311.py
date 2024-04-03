# Generated by Django 3.2.7 on 2024-01-09 17:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0073_auto_20240109_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispacthpostuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dispacthpostuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('ADMIN', 'ADMIN'), ('USER', 'USER'), ('SUPERVISIOR', 'SUPERVISIOR')], max_length=15),
        ),
        migrations.AlterField(
            model_name='dispatch_data',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 23, 11, 40, 990704)),
        ),
        migrations.AlterField(
            model_name='dispatchnumber',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 23, 11, 40, 991704)),
        ),
        migrations.AlterField(
            model_name='maciddata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='salesCreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 23, 11, 40, 992701)),
        ),
        migrations.AlterField(
            model_name='staticbarcode',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='storetype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 23, 11, 40, 994204)),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='updatedprice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('ADMIN', 'ADMIN'), ('USER', 'USER'), ('SUPERVISIOR', 'SUPERVISIOR')], max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_store', models.ManyToManyField(to='api.StoreType')),
            ],
        ),
    ]
