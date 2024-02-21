from django.contrib import admin
from .models import Articles,ImageArticles

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','id','date_created']
    search_fields = ['title','id']
    list_filter = ["date_created"]


class ImageArticlesAdmin(admin.ModelAdmin):
    list_display = ['image','id',]
    search_fields = ['id',]


admin.site.register(Articles,ArticleAdmin)
admin.site.register(ImageArticles,ImageArticlesAdmin)
