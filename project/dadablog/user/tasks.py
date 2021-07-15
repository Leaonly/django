from tools.sms import YunTongXin
from django.conf import settings
from dadablog.celery import app 

@app.task
def send_sms_c(phone, code):
    # 引用settings.py配置
    config = settings.MY_CONFIG

    yun = YunTongXin(**config)
    res = yun.run(phone, code)
    return res