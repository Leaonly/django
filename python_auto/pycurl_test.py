# -*- coding: utf-8  -*-

import os,sys
import time
import pycurl

URL='http://www.baidu.com'
c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)
c.setopt(pycurl.TIMEOUT, 5)
c.setopt(pycurl.NOPROGRESS, 1)
c.setopt(pycurl.FORBID_REUSE, 1)
c.setopt(pycurl.MAXREDIRS, 1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

# 创建文件 存储返回内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt",'wb')
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()
except Exception as e:
    print('connection error:'+str(e))
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(pycurl.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(pycurl.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(pycurl.PRETRANSFER_TIME)

STARTTRANSFER_TIME = c.getinfo(pycurl.STARTTRANSFER_TIME)

HTTP_CODE = c.getinfo(pycurl.HTTP_CODE)

# 打印输出相关数据
print('HTTP状态码：%s' % (HTTP_CODE))


indexfile.close()
c.close()
