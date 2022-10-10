# Generated by Django 4.1.2 on 2022-10-10 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop_app", "0004_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop_app.image",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(default="default.png", upload_to="book_covers"),
        ),
    ]
