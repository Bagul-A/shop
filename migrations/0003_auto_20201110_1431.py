# Generated by Django 3.1.2 on 2020-11-10 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201108_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]
