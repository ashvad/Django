# Generated by Django 4.0.3 on 2022-06-22 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_orders_expected_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 27, 20, 58, 30, 615677), null=True),
        ),
    ]
