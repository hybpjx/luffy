from celery import Celery

# 创建celery对象

app = Celery()

# 加载配置
app.config_from_object("Celery_tasks.config")

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')

django.setup()

# 注册任务
# app.autodiscover_tasks(['Celery_tasks.sms'])
app.autodiscover_tasks(['Celery_tasks.sms','Celery_tasks.mail'])

# 通过终端 启动celery
# celery -A Celery_tasks.main worker --loglevel=info
