import logging

from Celery_tasks.main import app
from django.conf import settings
from django.core.mail import send_mail
import os

from rest_framework import status
from rest_framework.response import Response
log=logging.getLogger("django")

@app.task(name="send_email")
def send_email(to_mail,password):
    if not os.getenv('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'luffyapi.settings.dev'
    subject = 'Luffy学习网——修改密码'  # 主题
    from_email = settings.EMAIL_FROM  # 发件人，在settings.py中已经配置
    to_email = to_mail  # 邮件接收者列表
    # 发送的消息
    message = f'您好，您的密码重置为：{password}'  # 发送普通的消息使用的时候message
    # meg_html = '<a href="http://www.baidu.com">点击跳转</a>'  # 发送的是一个html消息 需要指定
    ret = send_mail(subject, message, from_email, [to_email])
    if ret:
        # return Response({"message": "OK,邮件已经发送成功!"})
        log.info(f"{to_mail}:发送邮件成功")
    else:
        log.error(f"{to_mail}:发送邮件失败")
        # return Response({"message": "OK,邮件已经发送成功!"}, status=status.HTTP_400_BAD_REQUEST)