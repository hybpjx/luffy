from ronglian_sms_sdk import SmsSDK

accId = '8aaf0708809721d00180a2bfbd2c023d'
accToken = '8cc08a0b6750491899ec96cae3ae8273'
appId = '8aaf0708809721d00180a2bfbe320243'


def send_message(to_mobile, datas: tuple, tid):
    sdk = SmsSDK(accId, accToken, appId)
    tid = tid
    mobile = to_mobile
    datas = datas
    resp = sdk.sendMessage(tid, mobile, datas)

    return resp


# print(send_message("17772231096", ('1234', '3'), "1"))
