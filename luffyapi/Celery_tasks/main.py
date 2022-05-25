from celery import Celery
# 创建celery对象

app = Celery()

# 加载配置
app.config_from_object("Celery_tasks.config")


# 注册任务
app.autodiscover_tasks(['Celery_tasks.sms'])
# app.autodiscover_tasks(['Celery_tasks.sms','Celery_tasks_mail'])



# 通过终端 启动celery

