from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    phone_number = models.CharField(max_length=20,verbose_name='Номер телефона')
    is_agreed = models.BooleanField(verbose_name='Соглашение')

    class Meta:
        verbose_name = ("Контакты")
        verbose_name_plural = ("Контакты")
        ordering = ['-id']
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class FAQ(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок Вопроса')
    response = models.TextField(verbose_name='Ответ')

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/',verbose_name='Картинка')
    to_show = models.BooleanField(verbose_name='Показать')
    ordering = ['-id']


    class Meta:
        verbose_name = _("Галерея")
        verbose_name_plural = _("Галереи")
        indexes = [
            models.Index(fields=['id']), 
        ]

    def __str__(self):
        return f'{self.to_show}'
