from django.contrib import admin
from .models import Reviews

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name','subtitle']
    search_fields = ['full_name','subtitle']
    list_filter = ['subtitle']

admin.site.register(Reviews,ReviewAdmin)