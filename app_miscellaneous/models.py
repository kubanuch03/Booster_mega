from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_agreed = models.BooleanField()

    class Meta:
        verbose_name = _("contact_us")
        verbose_name_plural = _("contact_us")

    def __str__(self):
        return f'{self.name}'





class FAQ(models.Model):
    title = models.CharField(max_length=255)
    response = models.TextField()

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ")

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    to_show = models.BooleanField()

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallerys")

    def __str__(self):
        return f'{self.to_show}'
