# Generated by Django 4.0.3 on 2023-03-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0074_cart_notification_alter_paymentorder_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryy',
            name='deactivated_products',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='order_date',
            field=models.TextField(default='2023-03-06 13:58:15.813110+05:30'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='created_at',
            field=models.TextField(default='2023-03-06 13:58:15.813110+05:30'),
        ),
    ]