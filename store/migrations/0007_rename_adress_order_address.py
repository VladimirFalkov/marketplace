# Generated by Django 4.2.1 on 2023-06-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_order_alter_product_image_orderitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="adress",
            new_name="address",
        ),
    ]
