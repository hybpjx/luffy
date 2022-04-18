from django.db import DatabaseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
import logging

logger = logging.getLogger("django")


# 自定义的异常方法
def custom_exception_handler(exc, context):
    """
    自定义异常类
    :exc: 本次发生请求的异常信息
    :context: 本次请求发生的异常的执行上下午(本次请求的request,异常发送的时间,行号等)
    """
    response = exception_handler(exc, context)

    # 从内容字典里取出来视图内容
    view = context.get("view")

    if response is None:
        """
        如果进到这个判断里 只有两种情况
        1. 程序没有报错
        2. 出错了 Django本身与rest_framework没有识别到此次错误
        """
        if isinstance(exc, DatabaseError):
            # 数据库异常
            logger.error(f"[{view}] {exc}")
            response = Response({"message":"服务器内部错误 请尽快联系管理员"},status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response