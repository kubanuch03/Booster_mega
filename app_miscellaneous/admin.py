from django.contrib import admin

from .models import (
    Gallery,
    ContactUs,
    FAQ
)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','id','phone_number','is_agreed',]
    list_filter = ['id','is_agreed',]


class FAQAdmin(admin.ModelAdmin):
    list_display = ['title','id','response',]
    list_filter = ['id']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image','to_show',]
    list_filter = ['id','to_show',]





admin.site.register(Gallery,GalleryAdmin)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(ContactUs,ContactUsAdmin)