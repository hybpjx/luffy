from django.contrib import admin

# Register your models here.
# 装饰器注册
from . import models


@admin.register(models.Banner)
class BannerModelAdmin(admin.ModelAdmin):
    """轮播图"""
    list_display = ('title', 'orders', 'is_show',)


@admin.register(models.Navigation)
class NavModelAdmin(admin.ModelAdmin):
    """导航菜单"""
    list_display = ('title','link','is_site', 'position','orders', 'is_show',)


admin.site.site_header = "路飞学城"
admin.site.index_title = "路飞学城"
admin.site.site_title = "路飞学城"
