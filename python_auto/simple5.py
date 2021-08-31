#!/user/bin/python3

import dns.resolver
import os
import httplib2 , requests

iplist=[]
appdomain="www.baidu.com"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print('dns resolver error: '+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    try:
        conn=requests.get(checkurl, timeout=5)
        conn.encoding = conn.apparent_encoding
        return conn
    except Exception as e  :
        print(e)

if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print('dns resolver error.')

