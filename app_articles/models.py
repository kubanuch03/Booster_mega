from django.db import models
from django.utils.translation import gettext_lazy as _


class Articles(models.Model):
    title = models.CharField(max_length=255,verbose_name='Загаловка')
    images = models.ManyToManyField("ImageArticles",verbose_name='Картинка')
    short_description = models.TextField(verbose_name='Краткое Описание')
    description = models.TextField(verbose_name='Описание')
    date_created = models.DateField(verbose_name='Дата создание')

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")

    def __str__(self):
        return f'{self.title}'

class ImageArticles(models.Model):
    image = models.ImageField(upload_to="articles/%Y/%m/", verbose_name='Картинка')

    class Meta:
        verbose_name = _("Изображение Новостей")
        verbose_name_plural = _("Изображения Новостей")
        ordering = ['-id']

    def __str__(self):
        return f'{self.image}'