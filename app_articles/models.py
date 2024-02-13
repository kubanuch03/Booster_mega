from django.db import models
from django.utils.translation import gettext_lazy as _


class Articles(models.Model):
    title = models.CharField(max_length=255)
    images = models.ImageField(upload_to="articles/%Y/%m/")
    short_description = models.TextField()
    description = models.TextField()
    date_created = models.DateField()

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return f'{self.title}'
