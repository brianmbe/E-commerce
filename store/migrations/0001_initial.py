# Generated by Django 4.2 on 2023-04-09 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.IntegerField()),
                (
                    "main_picture",
                    models.ImageField(
                        default="product_mgs/1.jpg", upload_to="product_mgs/"
                    ),
                ),
                ("stock", models.IntegerField()),
                ("is_available", models.BooleanField(default=True)),
                ("created_date", models.DateTimeField()),
                ("modified_date", models.DateTimeField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="category.category",
                    ),
                ),
            ],
        ),
    ]
