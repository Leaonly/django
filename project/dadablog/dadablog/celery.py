from celery import Celery
from django.conf import settings
import os 

# 添加settings环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dadablog.settings')

app = Celery('dadablog')
app.conf.update(
    BROKER_URL = 'redis://:@192.168.170.136:6379/1'
)
# 自动注册应用下寻找加载worker函数
app.autodiscover_tasks(settings.INSTALLED_APPS)
