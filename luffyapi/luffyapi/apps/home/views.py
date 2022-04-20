from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from .models import Banner
from .serializers import BannerModelSerializers


class BannerListApiView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True,is_deleted=False,).order_by("-orders","-id")
    serializer_class = BannerModelSerializers
