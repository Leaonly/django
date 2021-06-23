import redis
import json

r = redis.Redis(host='192.168.170.136', port=6379, db=0, password='123456')

# r.setbit('pybit1', 4, 1)
# print(r.getbit('pybit1', 3))
# print(r.getbit('pybit1', 4))

print(r.bitcount('pybit1'))













