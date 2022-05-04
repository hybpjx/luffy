import re

from django.db.models import Q


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义 jwt认证成功返回数据
    :params token   本次登陆成功以后 , 返回的jwt
    :params user    本次登陆成功以后 从数据库中查询到的用户模型对象
    :params request 本次客户端的请求对象
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }


# 如果以后增加了什么邮箱登陆等选项 可以单独写个函数
def get_user_by_account(account):
    """
    根据账号 手机 来获取账号信息
    :params account: 账号 可以是用户名Username 也可以是手机mobile 或者是其他
    :return User对象 或者是None
    """
    try:
        # if re.match(r"^1[3-9]\d{9}$",account):
        #     # 账号是手机号
        #     user = User.objects.get(mobile=account)
        # else:
        #     # 账号为用户名
        #     user = User.objects.get(username=account)

        # 上面方法 是用if else判断 也可以用Q对象判断
        user = User.objects.filter(Q(username=account) | Q(mobile=account)).first()

    except User.DoesNotExist:
        return None
    else:
        return user

from .models import User
from django.contrib.auth.backends import ModelBackend


class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
            密码不能直接作校验 因为密码是通过加密的
            通过Q对象 做多条件查询
            user = User.objects.filter(Q(username=username) | Q(mobile=username)).first()
        """
        # 这里直接引用函数 目的是为了扩容
        user=get_user_by_account(account=username)
        # 验证 如果存在 且 检查user密码和权限
        if user and user.check_password(password) and user.is_authenticated:
            return user
        else:
            # 否则 则什么都不返回
            return None

