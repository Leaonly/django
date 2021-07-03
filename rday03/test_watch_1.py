import redis 
import time
from redis.connection import ConnectionPool 

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379, password=123456)
r = redis.Redis(connection_pool=pool)

def double_account(user_id):

    key = 'account_%s'%(user_id)
    # transaction是否开启事务
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                pipe.watch(key)
                value = int(r.get(key))
                value *= 2
                pipe.multi()
                pipe.set(key, value)
                pipe.execute()
                break
            except redis.WatchError:
                print('----key changed')
                continue
    return int(r.get(key))

if __name__ == '__main__':

    print(double_account('leaon'))

    