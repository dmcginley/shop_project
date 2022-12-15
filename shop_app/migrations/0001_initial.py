# Generated by Django 4.1.2 on 2022-12-15 00:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(db_index=True, max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
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
                    "image",
                    models.ImageField(default="no_cover.png", upload_to="book_covers/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
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
                    "name",
                    models.CharField(
                        help_text="The name of the Publisher.", max_length=100
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                    "title",
                    models.CharField(
                        help_text="The title of the book.", max_length=255
                    ),
                ),
                (
                    "rating",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="Between 1 and 10",
                        max_digits=2,
                    ),
                ),
                ("description", models.TextField(blank=True)),
                (
                    "isbn",
                    models.CharField(
                        max_length=20, verbose_name="ISBN number of the book."
                    ),
                ),
                (
                    "publication_date",
                    models.DateField(
                        help_text="e.g. 2022-10-29",
                        null=True,
                        verbose_name="Date the book was published.",
                    ),
                ),
                ("pages", models.PositiveIntegerField(null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=4)),
                ("number_in_stock", models.PositiveIntegerField(blank=True, null=True)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("authors", models.ManyToManyField(to="shop_app.author")),
                (
                    "genres",
                    models.ManyToManyField(
                        help_text="Select a genre for this book",
                        related_name="book",
                        to="shop_app.genre",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.image",
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.publisher",
                    ),
                ),
            ],
            options={
                "ordering": ("-date_added",),
            },
        ),
    ]
