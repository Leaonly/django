import redis

r = redis.Redis(host='192.168.170.136', port=6379, db=0, password='123456')

# 基础命令
key_list = r.keys('*')
# print(key_list)
# [b'test', b'uuname', b'trill:fansnumber', b'n1', b'l1', b'k1', b'trill:username', b'trill:gender', b'spider:urls', b'k2', b'trill:password']
#print(r.type('l1'))

## list
#r.lpush('pyl1', 'a', 'v', 'w', 'z')
#print(r.lrange('pyl1',0,-1))
#r.linsert('pyl1','before', 'v','g')
# print(r.lrange('pyl1',0,-1))

## string
r.set('puname', 'guoxiaonao',ex=30)
print(r.get('puname'))
r.mset({'k1':'v1','k2':'v2'})
print(r.mget('k1','k2','k3'))

