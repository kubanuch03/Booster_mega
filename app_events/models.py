from django.db import models
from django.utils.translation import gettext_lazy as _


class Events(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    datetime = models.DateTimeField(verbose_name='Дата')
    datetime_event = models.DateTimeField(verbose_name='Дата Ивента')
    image = models.ImageField(upload_to='event_images/',verbose_name='Изображение')
    extended_image = models.ImageField(upload_to='extended_event_images/',verbose_name='Иконка')
    duration = models.CharField(max_length=255,verbose_name='Продолжительность')
    speaker_name = models.CharField(max_length=255,verbose_name='Спикер')
    free_spots = models.IntegerField(verbose_name='Свободные места')

    class Meta:
        verbose_name = _("Ивент")
        verbose_name_plural = _("Ивенты")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'
