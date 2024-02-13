from django.contrib import admin

from .models import (
    Gallery
)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image','to_show']
    list_filter = ['to_show']

admin.site.register(Gallery,GalleryAdmin)