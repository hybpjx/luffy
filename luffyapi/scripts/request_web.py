import requests

data = {
    "mobile": "13332231096",
    "sms_code": "4444",
    "password": "admin*123"
}
print(requests.post("http://api.luffy.cn:8000/user/", data=data).text)
