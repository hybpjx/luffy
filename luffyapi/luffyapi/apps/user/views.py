import random

from django.contrib import auth
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework.views import APIView
from django_redis import get_redis_connection

from .models import User
from .utils import get_user_by_account
from luffyapi.libs.geetest import GeetestLib
from .serializers import UserModelSerializers

from luffyapi.settings import constant

captcha_id = "5033a47b10bb9628efd44289e49636aa"
private_key = "b91e188f42ce8c0c57ed21f8754c22cf"


class CaptchaAPIView(APIView):
    """
    验证码视图类
    """

    # 增加个常量 防止后续不会报错
    status = False
    user_id = 0

    def get(self, request):
        """获取验证码的功能"""
        # 先拿到前端请求的username
        # username = request.data.username
        username = request.query_params.get("username")
        # 再通过请求的username 拿到用户 最终拿到ID
        user = get_user_by_account(username)
        if user is None:
            return Response({"message": "对不起,用户不存在"}, status=http_status.HTTP_400_BAD_REQUEST)
        self.user_id = user.id
        gt = GeetestLib(captcha_id, private_key)
        self.status = gt.pre_process(self.user_id)
        # todo: 后面增加 status和 user_id 保存在redis数据库中
        response_str = gt.get_response_str()
        return Response(response_str)

    def post(self, request):
        """验证码的验证方法"""
        gt = GeetestLib(captcha_id, private_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        if self.status:
            result = gt.success_validate(challenge, validate, seccode, self.user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        # 不需要 json.dumps(result) 因为已经默认是Json了
        return Response(result)


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializers


import re


class ModelAPIView(APIView):
    def get(self, request, mobile):
        # # 验证手机号码的格式 !! 已经在url声明过了
        if not re.match(r"^1[3-9]\d{9}$", mobile):
            return Response({"message": "对不起,手机号码 格式错误"}, status=http_status.HTTP_400_BAD_REQUEST)
        # 验证 手机号是否被注册过
        if get_user_by_account(mobile):
            return Response({"message": "对不起,手机号码已经被注册了"}, status=http_status.HTTP_400_BAD_REQUEST)
        return Response({"message": "ok 可以使用"}, status=http_status.HTTP_200_OK)


# 不需要验证太多信息
class SMSAPIView(APIView):

    def get(self, request, mobile):
        """短信发送接口"""

        # 1. 判断短信 60秒内是否发送
        redis_conn = get_redis_connection("sms_code")
        ret = redis_conn.get(f"mobile_{mobile}")
        if ret:
            return Response({"message": "对不起 请勿频繁发送短信 请60秒后重试"}, status=http_status.HTTP_400_BAD_REQUEST)

        # 2. 生成短信验证码
        sms_code = "%06d" % random.randint(1, 999999)  # 生成六位数字

        # 3. 保存短信验证码到redis中[使用事务把多条指令集中发送给redis数据库]
        # 创建一个管道对象
        pipe=redis_conn.pipeline()
        # 开启事务[无法管理数据库的数据读取操作]
        pipe.multi()
        # 把事务中要完成的所有操作，写入管道中
        pipe.setex(f"sms_{mobile}", constant.SMS_EXPIRE_TIME, sms_code)
        pipe.setex(f"mobile_{mobile}", constant.SMS_INTERVAL_TIME, "-")
        # 执行事务
        pipe.execute()

        try:
            from Celery_tasks.sms.tasks import send_sms

            send_sms.delay(mobile,sms_code)

            return Response({"message": "发送短信成功"})
        except:
            return Response({"message": "发送短信失败"}, status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)



class ForgetAPIView(APIView):
    def get(self, request, email):
        """邮件发送"""

        # 验证 手机号是否被注册过
        if not get_user_by_account(email):
            return Response({"message": "对不起,邮箱尚未注册，请先注册"}, status=http_status.HTTP_400_BAD_REQUEST)

        # 1. 判断短信 60秒内是否发送
        redis_conn = get_redis_connection("mail_code")
        ret = redis_conn.get(f"email_{email}")
        if ret:
            return Response({"message": "对不起 请勿频繁发送邮件 请60秒后重试"}, status=http_status.HTTP_400_BAD_REQUEST)

        # 2. 生成密码
        now_password = "%06d" % random.randint(1, 999999)  # 生成六位数字

        # 3. 保存短信验证码到redis中[使用事务把多条指令集中发送给redis数据库]
        # 创建一个管道对象
        pipe = redis_conn.pipeline()
        # 开启事务[无法管理数据库的数据读取操作]
        pipe.multi()
        # 把事务中要完成的所有操作，写入管道中
        pipe.setex(f"password_{email}", constant.SMS_EXPIRE_TIME, now_password)
        pipe.setex(f"mail_{email}", constant.SMS_INTERVAL_TIME, "-")
        # 执行事务
        pipe.execute()

        try:
            from Celery_tasks.mail.tasks import send_email

            send_email.delay(email,now_password)
            try:
                user = User.objects.get(email=email)
                user.password = make_password(now_password)

                if user:
                    user.save()
                    return Response({"message": "请查看邮箱"})

                else:
                    return Response({"message": "修改密码失败 可能是用户不存在"},status=http_status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"message": "用户不存在"},status=http_status.HTTP_404_NOT_FOUND)


        except:
            return Response({"message": "发送邮件失败"}, status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)
