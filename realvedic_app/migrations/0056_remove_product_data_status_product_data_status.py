# Generated by Django 4.0.3 on 2023-02-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0055_product_data_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_data',
            name='Status',
        ),
        migrations.AddField(
            model_name='product_data',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]