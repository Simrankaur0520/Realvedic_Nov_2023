# Generated by Django 4.0.3 on 2023-02-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0050_rename_token_paymentorder_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentorder',
            name='order_status',
            field=models.TextField(blank=True),
        ),
    ]
