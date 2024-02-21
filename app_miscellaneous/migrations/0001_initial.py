# Generated by Django 5.0.1 on 2024-02-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("is_agreed", models.BooleanField()),
            ],
            options={
                "verbose_name": "Контакты",
                "verbose_name_plural": "Контакты",
                "indexes": [
                    models.Index(fields=["id"], name="app_miscell_id_ac720a_idx"),
                    models.Index(fields=["name"], name="app_miscell_name_25c129_idx"),
                ],
            },
        ),
        migrations.CreateModel(
            name="FAQ",
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
                ("title", models.CharField(max_length=255)),
                ("response", models.TextField()),
            ],
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "FAQ",
                "indexes": [
                    models.Index(fields=["id"], name="app_miscell_id_95671d_idx"),
                    models.Index(fields=["title"], name="app_miscell_title_50445f_idx"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="gallery_images/")),
                ("to_show", models.BooleanField()),
            ],
            options={
                "verbose_name": "Галерея",
                "verbose_name_plural": "Галереи",
                "indexes": [
                    models.Index(fields=["id"], name="app_miscell_id_2fbf82_idx")
                ],
            },
        ),
    ]
