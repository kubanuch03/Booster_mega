# Generated by Django 5.0.1 on 2024-02-14 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_miscellaneous", "0002_rename_image_gallery_delete_reviews"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gallery",
            options={"verbose_name": "Gallery", "verbose_name_plural": "Gallerys"},
        ),
    ]