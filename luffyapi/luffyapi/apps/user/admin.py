from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """导航菜单"""
    list_display = ('username','is_active','mobile','avatar','wxchat')
