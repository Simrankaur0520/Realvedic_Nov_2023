# Generated by Django 4.0.3 on 2023-02-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0058_alter_paymentorder_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentorder',
            name='order_date',
            field=models.TextField(default='2023-02-28 12:52:03.378118+05:30'),
        ),
    ]
