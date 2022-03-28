#!/usr/bin/env python3
import fabric


host='192.168.129.135'
conn = fabric.Connection(host=host, user='root', connect_kwargs={'password':'123456'})


def host_type():
    print('%s:'%host)
    conn.run('uname -s')


host_type()