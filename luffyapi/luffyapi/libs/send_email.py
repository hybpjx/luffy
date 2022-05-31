from django.conf import settings
from django.core.mail import send_mail
import os

from rest_framework import status
from rest_framework.response import Response


def send_email(to_email):
    if not os.getenv('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'luffyapi.settings.dev'
    subject = 'C语言中文网链接'  # 主题
    from_email = settings.EMAIL_FROM  # 发件人，在settings.py中已经配置
    to_email =to_email  # 邮件接收者列表
    # 发送的消息
    message = 'c语言中文网欢迎你点击登录 http://c.biancheng.net/'  # 发送普通的消息使用的时候message
    # meg_html = '<a href="http://www.baidu.com">点击跳转</a>'  # 发送的是一个html消息 需要指定
    ret=send_mail(subject, message, from_email, [to_email])
    if ret:
        return Response({"message":"OK,邮件已经发送成功!"})
    else:
        return Response({"message":"OK,邮件已经发送成功!"},status=status.HTTP_400_BAD_REQUEST)


if __name__ == '__main__':
    print(bool(1))