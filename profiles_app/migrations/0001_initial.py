# Generated by Django 4.1.2 on 2022-12-14 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop_app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop_app.book"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "default_name",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "default_phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "default_street_address1",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "default_street_address2",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "default_town_or_city",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "default_county",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "default_postcode",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "default_country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, null=True
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
