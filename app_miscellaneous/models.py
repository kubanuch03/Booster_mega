from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_agreed = models.BooleanField()

    class Meta:
        verbose_name = ("Контакты")
        verbose_name_plural = ("Контакты")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['name']),  
        ]

    def __str__(self):
        return f'{self.name}'


class FAQ(models.Model):
    title = models.CharField(max_length=255)
    response = models.TextField()

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
    image = models.ImageField(upload_to='gallery_images/')
    to_show = models.BooleanField()

    class Meta:
        verbose_name = _("Галерея")
        verbose_name_plural = _("Галереи")
        indexes = [
            models.Index(fields=['id']), 
        ]

    def __str__(self):
        return f'{self.to_show}'
