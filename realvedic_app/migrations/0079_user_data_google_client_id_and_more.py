# Generated by Django 4.1.5 on 2023-10-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0078_alter_paymentorder_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='google_client_id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='order_date',
            field=models.TextField(default='2023-10-06 13:20:38.353606+05:30'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='created_at',
            field=models.TextField(default='2023-10-06 13:20:38.353606+05:30'),
        ),
    ]
