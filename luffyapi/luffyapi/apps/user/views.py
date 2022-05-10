from django.shortcuts import render
# coding:utf-8
import json

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework.views import APIView

from .models import User
from .utils import get_user_by_account
from luffyapi.libs.geetest import GeetestLib
from .serializers import UserModelSerializers

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
        # if not re.match(r"^1[3-9]\d{9}$", mobile):
        #     return Response({"message": "对不起,手机号码 格式错误"})

        # 验证 手机号是否被注册过
        if get_user_by_account(mobile):
            return Response({"message": "对不起,手机号码已经被注册了"},status=http_status.HTTP_400_BAD_REQUEST)
        return Response({"message":"注册成功"},status=http_status.HTTP_200_OK)
