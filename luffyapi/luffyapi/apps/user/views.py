from django.shortcuts import render
# coding:utf-8
import json

from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework.views import APIView
from luffyapi.apps.user.utils import get_user_by_account
from luffyapi.libs.geetest import GeetestLib

captcha_id = "b46d1900d0a894591916ea94ea91bd2c"
private_key = "36fc3fe98530eea08dfc6ce76e3d24c4"



class CaptchaAPI(APIView):
    """
    验证码视图类
    """

    # 增加个常量 防止后续不会报错
    status = False
    user_id = 0

    def get(self,request):
        """获取验证码的功能"""
        # 先拿到前端请求的username
        username = request.data.username
        # 再通过请求的username 拿到用户 最终拿到ID
        user=get_user_by_account(username)
        if user is None:
            return Response({"message":"对不起,用户不存在"},status=http_status.HTTP_400_BAD_REQUEST)
        self.user_id = user.id
        gt = GeetestLib(captcha_id, private_key)
        self.status = gt.pre_process(self.user_id)
        # todo: 后面增加 status和 user_id 保存在redis数据库中
        response_str = gt.get_response_str()
        return Response(response_str)

    def post(self,request):
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

