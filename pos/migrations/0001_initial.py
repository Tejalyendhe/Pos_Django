# Generated by Django 3.2.7 on 2023-12-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemWithoutLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, default='', max_length=50)),
                ('code', models.CharField(blank=True, default='', max_length=10)),
                ('default_rate', models.FloatField(blank=True, default=0)),
                ('default_qty', models.FloatField(blank=True, default=1)),
            ],
        ),
    ]
