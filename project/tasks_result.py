from celery import Celery

app = Celery('gxn_result', broker='redis://:@192.168.170.136:6379/2',backend='redis://:@192.168.170.136:6379/3')

@app.task
def task_test(a, b):
    print('task is running...')
    return a + b