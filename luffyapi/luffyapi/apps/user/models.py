from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # 唯一索引
    mobile = models.CharField(max_length=15,unique=True, verbose_name="手机号")
    avatar = models.ImageField(upload_to="avatar",null=True,blank=True,verbose_name="用户头像")
    wxchat = models.CharField(max_length=64, verbose_name="微信号")

    class Meta:
        db_table="luffy_user"
        verbose_name = "用户信息"
        verbose_name_plural=verbose_name