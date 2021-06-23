import redis
import json

r = redis.Redis(host='192.168.170.136', port=6379, db=0, password='123456')

json_obj = {'task':'send_email','email_body':'aaa','from':'bbb','to':'gxn'}
json_str = json.dumps(json_obj)
r.lpush('pyl2', json_str)