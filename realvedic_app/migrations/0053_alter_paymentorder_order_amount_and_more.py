# Generated by Django 4.0.3 on 2023-02-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0052_alter_paymentorder_order_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentorder',
            name='order_amount',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='order_payment_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='order_product',
            field=models.TextField(),
        ),
    ]
