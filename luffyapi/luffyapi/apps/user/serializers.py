from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import make_password
from django_redis import get_redis_connection
import re

from .utils import get_user_by_account
from .models import User


class UserModelSerializers(serializers.ModelSerializer):
    sms_code = serializers.CharField(min_length=4, max_length=6, write_only=True, required=True, help_text="验证码")

    token = serializers.CharField(max_length=1024, read_only=True, help_text="Token认证字符串")

    class Meta:
        model = User
        fields = ("id", "username", "token", "mobile", "sms_code")
        extra_kwargs = {
            "id": {
                "read_only": True,
            },
            "username": {
                "read_only": True,
            },
            "mobile": {
                "write_only": True,
            },
            "password": {
                "write_only": True,
            },
        }

    def validate(self, attrs):
        mobile = attrs.get("mobile")
        sms_code = attrs.get("sms_code")
        password = attrs.get("password")

        # 验证手机号码的格式

        if not re.match(r"^1[3-9]\d{9}$", mobile):
            raise serializers.ValidationError("对不起,手机号码 格式错误")

        # 验证 手机号是否被注册过
        if get_user_by_account(mobile):
            raise serializers.ValidationError("对不起,手机号码已经被注册了")

        #  验证验证码正确与否   接受客户端的验证码 和 真实验证码作对比

        redis_conn = get_redis_connection("sms_code")
        # 这里获取的数据是 bytes类型的字符串
        real_sms_code = redis_conn.get(f"sms_{mobile}")
        # 本次验证 直接删除本次验证码 防止出现密码爆破
        redis_conn.delete(f"sms_{mobile}")

        # 需要转码
        if real_sms_code.decode() != sms_code:
            raise serializers.ValidationError("对不起,验证码不正确，本次验证码已失效，请重新发送")

        return attrs

    def create(self, validated_data):
        """用户信息"""

        # 移除到不需要的数据
        validated_data.pop("sms_code")
        # 对密码进行加密
        raw_password = validated_data.get("password")
        hash_password = make_password(raw_password)  # 已经加密的密码
        # 对用户名设置一个默认的值
        username = validated_data.get("mobile")
        # 调用序列化器提供的方法
        user = User.objects.create(
            username=username,
            password=hash_password,
            mobile=username
        )

        # 使用 restframework_jwt提供的手动生成Token的方法

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user
