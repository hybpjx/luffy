from Celery_tasks.main import app
from luffyapi.libs.yuntongxun.update_sms import send_message
from luffyapi.settings import constant
import logging

log=logging.getLogger("django")

@app.task(name="send_sms")
def send_sms(mobile,sms_code):
    # 4. 调用短信sdk 发送短信
    ret = send_message(mobile, (sms_code, constant.SMS_INTERVAL_TIME // 60), constant.SMS_TEMPLATE_ID)
    ret = eval(ret)
    # 5. 短信发送成功返回的结果
    if ret.get("statusCode") == "000000":
        # 发送短信成功
        log.info(f"{mobile}:发送短信成功")
    else:
        log.error(f"{mobile}:发送短信失败")


