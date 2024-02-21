from django.contrib import admin

from .models import Events

class EventAdmin(admin.ModelAdmin):
    list_display = ['title','datetime','speaker_name']
    list_filter = ['id','speaker_name','duration']
    search_fields = ['id','speaker_name','duration']

admin.site.register(Events,EventAdmin)