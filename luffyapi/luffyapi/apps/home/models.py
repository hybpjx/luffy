from django.db import models


# Create your models here.
class Banner(models.Model):
    """
    轮播图模型对象
    """
    # 模型字段
    title = models.CharField(max_length=255, verbose_name="广告标题")
    link = models.CharField(max_length=255, verbose_name="广告链接")
    # 文件存储的目录 用于保存图片
    image_url = models.ImageField(upload_to="banner",max_length=255, verbose_name="广告图片")
    remark = models.TextField(verbose_name="备注信息")
    is_show = models.BooleanField(default=False, verbose_name="是否显示")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")

    # 表信息声明
    class Meta:
        db_table = "luffy_banner"
        verbose_name = "轮播广告"
        verbose_name_plural = verbose_name

    # 自定义方法|自定义字段|自定义工具
    def __str__(self):
        return self.title
