# Generated by Django 4.0.3 on 2022-07-20 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_orders_expected_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 25, 13, 42, 33, 433973), null=True),
        ),
    ]
