# Generated by Django 5.0.1 on 2024-02-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="image",
            field=models.ImageField(
                upload_to="event_images/", verbose_name="Изображение"
            ),
        ),
    ]