# Generated by Django 4.1.2 on 2022-11-27 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("checkout_app", "0002_order_original_cart_order_stripe_pid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderlineitem",
            old_name="product",
            new_name="book",
        ),
    ]
