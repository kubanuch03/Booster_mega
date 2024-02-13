from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

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

admin.site.unregister(User) 
admin.site.unregister(Group) 
 # Отменяем регистрацию стандартного администратора групп
# admin.site.register(Group, GroupAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
