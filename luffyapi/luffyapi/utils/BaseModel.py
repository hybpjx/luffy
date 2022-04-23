from django.db import models


class BaseModel(models.Model):
    is_show = models.BooleanField(default=False, verbose_name="是否显示")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    updated_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        """
        如果不指定abstract  = True 会导致 多出一个BaseModel的表
        """
        # 说明是一个抽象模型类
        abstract = True