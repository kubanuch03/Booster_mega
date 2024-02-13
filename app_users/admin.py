from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_users.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # model = CustomUser

    list_display = [
        "id",
        "username",
        "email",
        "phone_number",
        "created_at",
    ]
    search_fields = ("username", "email", "phone_number", "created_at")
    list_filter = ("is_staff", "created_at")

admin.site.register(CustomUser, CustomUserAdmin)
