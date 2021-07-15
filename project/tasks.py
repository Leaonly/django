from celery import Celery

app = Celery('gxn', broker='redis://:@192.168.170.136:6379/2')

@app.task
def task_test():
    print('task is running...')