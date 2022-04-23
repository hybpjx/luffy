from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from .models import Banner,Navigation
from .serializers import BannerModelSerializer,NavModelSerializer
from luffyapi.settings import constant


class BannerListApiView(ListAPIView):
    """轮播图广告视图"""
    queryset = Banner.objects.filter(is_show=True,is_deleted=False,).order_by("-orders","-id")[:constant.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class HeaderNavListApiView(ListAPIView):
    """头部导航栏菜单视图"""
    queryset = Navigation.objects.filter(is_show=True,is_deleted=False,position=1).order_by("-orders","-id")[:constant.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class FooterNavListApiView(ListAPIView):
    """脚部导航栏菜单视图"""
    queryset = Navigation.objects.filter(is_show=True,is_deleted=False,position=2).order_by("-orders","-id")[:constant.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer
