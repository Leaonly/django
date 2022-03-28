import dns.resolver
import http.client

iplist=[]
appdomain="www.baidu.com"

def get_iplist(domain=""):
    try:
        A = dns.resolver.resolve(domain, 'A')
    except Exception as e:
        print('dns resolver error:' + str(e))
        return None
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j)
    return True

def checkip(ip):
    checkurl=str(ip)+":80"
    getcontent=""
    code=None
    # 创建http连接
    conn=http.client.HTTPConnection(checkurl,timeout=5)
    try:
        # 发起URL请求，添加http连接对象
        conn.request("GET","/",headers={"Host": appdomain})
        r = conn.getresponse()
        # 获取URL页面前15的字符，以便做可用性校验
        getcontent = r.read(15)
        # 获取状态码
        code = r.code
    finally:
        if getcontent=="<!DOCTYPE HTML>":
            print(str(ip) + " [OK]")
        elif code in [200, 301, 302, 304]:
            print(str(ip) + " [OK]")
        else:
            print(str(ip) + " [Error]")

if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print('dns resolver error.')
