from django.db import models
from django.utils.translation import gettext_lazy as _


class Events(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    extended_image = models.ImageField(upload_to='extended_event_images/')
    datetime = models.DateTimeField()
    duration = models.CharField(max_length=255)
    speaker_name = models.CharField(max_length=255)
    free_spots = models.IntegerField()

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return f'{self.name}'
