# Generated by Django 3.2.7 on 2024-01-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_auto_20240104_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billdiscount',
            name='discount_class',
        ),
        migrations.AddField(
            model_name='billdiscount',
            name='discount_icon',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
