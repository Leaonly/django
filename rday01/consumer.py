import redis
import json

r = redis.Redis(host='192.168.170.136', port=6379, db=0, password='123456')

while True:
    task = r.brpop('pyl2', 10)
    print(task)
    if task:
        json_obj = json.loads(task[1])
    else:
        print('---no task---')
    break