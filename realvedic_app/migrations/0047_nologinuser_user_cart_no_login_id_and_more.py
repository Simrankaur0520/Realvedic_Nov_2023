# Generated by Django 4.0.3 on 2023-02-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0046_product_data_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='noLoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user_cart',
            name='no_login_id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user_cart',
            name='user_id',
            field=models.TextField(blank=True),
        ),
    ]