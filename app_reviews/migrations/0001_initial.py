# Generated by Django 5.0.1 on 2024-02-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                ("full_name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="reviews/")),
                ("subtitle", models.CharField(max_length=100)),
                ("review_text", models.TextField()),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
                "indexes": [
                    models.Index(fields=["id"], name="app_reviews_id_beb88e_idx"),
                    models.Index(
                        fields=["full_name"], name="app_reviews_full_na_f2320b_idx"
                    ),
                ],
            },
        ),
    ]
