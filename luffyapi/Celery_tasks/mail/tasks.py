from Celery_tasks.main import app


@app.task(name="send_main")
def send_mail():
    """发送邮件"""
    return "hello,mail!!!!"