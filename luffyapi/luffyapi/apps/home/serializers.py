from rest_framework import serializers

from .models import Banner, Navigation


class BannerModelSerializer(serializers.ModelSerializer):
    # 字段声明

    # 模型化序列化器声明
    class Meta:
        model = Banner
        # fields="__all__"
        fields = ["title", "image_url", "link", ]
    # 验证方法
    # 存储数据方法


class NavModelSerializer(serializers.ModelSerializer):
    # 字段声明

    # 模型化序列化器声明
    class Meta:
        model = Navigation
        # fields="__all__"
        fields = ["title", "link", "position", "is_site"]
    # 验证方法
    # 存储数据方法
