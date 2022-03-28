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

'''
c = pycurl.Curl()                    #创建一个curl对象
c.setopt(pycurl.CONNECTTIMEOUT,5)        #连接的等待时间，设置为0则不等待
c.setopt(pycurl.TIMEOUT,5)                    #请求超时时间
c.setopt(pycurl.NOPROGRESS,0)            #是否屏蔽下载进度条，非0则屏蔽
c.setopt(pycurl.MAXREDIRS,5)                #指定HTTP重定向的最大数
c.setopt(pycurl.FORBID_REUSE,1)            #完成交互强制断开连接，不重复
c.setopt(pycurl.FRESH_CONNECT,1)            #强制获取新的连接，即替代缓存中的连接
c.setopt(pycurl.DNS_CACHE_TIMEOUT,60)        #设置保存DNS信息的时间，默认为120秒
c.setopt(pycurl.URL,"http://www.baidu.com")        #指定请求的URL
c.setopt(pycurl.USERAGENT,"Mozilla/5.2 (compatible;MSIE 6.0;Windows NT 5.1;SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)")    #配置请求HTTP头的User-Agent
c.setopt(pycurl.HEADERFUNCTION,getheader)        #将返回的HTTP HEADER定向到回调函数getheader
c.setopt(pycurl.WRITEFUNCTION,getbody)        #将返回的内容定向到回调函getbody
c.setopt(pycurl.WRITEHEADER,fileobj)            #将返回的HTTP HEADER定向到fileobj文件对象
c.setop(pucurl.WRITEADTA,fileobj)            #将返回的HTML内容定向到fileobj文件对象

c = pycurl.Curl()                    #创建一个curl对象
c.getinfo(pycurl.HTTP_CODE)            #返回的HTTP状态码
c.getinfo(pycurl.TOTAL_TIME)            #传输结束所消耗的总时间
c.getinfo(pycurl.NAMELOOKUP_TIME)        #DNS解析所消耗的时间
c.getinfo(pycurl.CONNECT_TIME)                #建立连接所消耗的时间
c.getinfo(pycurl.PRETRANSFER_TIME)            #从建立连接到准备传输所消耗的时间
c.getinfo(pycurl.STARTTRANSFER_TIME)         #从建立连接到传输开始消耗的时间
c.getinfo(pycurl.REDIRECT_TIME)                #重定向所消耗的时间
c.getinfo(pycurl.SIZE_UPLOAD)                    #上传数据包大小
c.getinfo(pycurl.SIZE_DOWNLOAD)                #下载数据包大小
c.getinfo(pycurl.SPEED_DOWNLOAD)               #平均下载速度
c.getinfo(pycurl.SPEED_UPLOAD)                    #平均上传速度
c.getinfo(pycurl.HEADER_SIZE)                    #HTTP头部大小
'''