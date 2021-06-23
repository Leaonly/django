import redis
import json

r = redis.Redis(host='192.168.170.136', port=6379, db=0, password='123456')

r.hmset('pyh1',{'name':'wwc','age':60})
print(r.hgetall('pyh1'))
