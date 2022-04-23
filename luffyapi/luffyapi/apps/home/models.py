from django.db import models

from luffyapi.utils.BaseModel import BaseModel




# Create your models here.
class Banner(BaseModel):
    """
    轮播图模型对象
    """
    # 模型字段
    title = models.CharField(max_length=255, verbose_name="广告标题")
    link = models.CharField(max_length=255, verbose_name="广告链接")
    # 文件存储的目录 用于保存图片
    image_url = models.ImageField(upload_to="banner", max_length=255, verbose_name="广告图片")
    remark = models.TextField(verbose_name="备注信息")

    # 表信息声明
    class Meta:
        db_table = "luffy_banner"
        verbose_name = "轮播广告"
        verbose_name_plural = verbose_name

    # 自定义方法|自定义字段|自定义工具
    def __str__(self):
        return self.title


class Navigation(BaseModel):
    """
    导航栏模型对象
    """
    # 模型字段
    POSITION_CHOICES = (
        (1, "顶部导航"),
        (2, "脚部导航")
    )
    title = models.CharField(max_length=255, verbose_name="导航标题")
    link = models.CharField(max_length=255, verbose_name="导航链接")
    position = models.IntegerField(choices=POSITION_CHOICES, default=1, verbose_name="导航栏位置")
    is_site = models.BooleanField(default=False, verbose_name="是否是站外链接")

    # 表信息声明
    class Meta:
        db_table = "luffy_navigation"
        verbose_name = "导航菜单"
        verbose_name_plural = verbose_name

    # 自定义方法|自定义字段|自定义工具
    def __str__(self):
        return self.title
