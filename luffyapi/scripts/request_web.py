import requests


data ={
    "username":"root",
    "password":"admin*123"
}
print(requests.post("http://api.luffy.cn:8000/user/login/",data=data).text)