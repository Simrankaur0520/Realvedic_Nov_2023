# Generated by Django 4.0.3 on 2023-03-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0069_alter_images_and_banners_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='images_and_banners',
            name='mobile_image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='order_date',
            field=models.TextField(default='2023-03-02 17:04:12.316556+05:30'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='created_at',
            field=models.TextField(default='2023-03-02 17:04:12.315559+05:30'),
        ),
    ]
