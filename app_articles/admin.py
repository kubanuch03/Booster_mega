from django.contrib import admin
from .models import Articles

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','id','date_created']
    search_fields = ['title','id']
    list_filter = ["date_created"]



admin.site.register(Articles,ArticleAdmin)
