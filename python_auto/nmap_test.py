# -*- coding: utf-8  -*-

import sys, os
import nmap

scan_row=[]
input_data = input('pls input hosts and port: ')
scan_row = input_data.split(' ')
if len(scan_row) != 2:
    print('input error')
    sys.exit(0)

hosts = scan_row[0]
port = scan_row[1]

class Logger(object):
    def __init__(self, filename='scan_list.txt'):
        self.terminal = sys.stdout
        self.log = open(filename, 'a') 

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# path = os.path.abspath(os.path.dirname(__file__))
# type = sys.getfilesystemencoding()
sys.stdout = Logger()



try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print('Unexcepted error')
    sys.exit(0)

try:
    # 调用扫描方法，参数指定扫描主机hosts
    nm.scan(hosts=hosts, arguments=' -v -sS -p '+port)
except Exception as e :
    print('Scan error: '+str(e))


# with open('/app/django/python_auto/scan_list.txt','a+') as f:
#     sys.stdout = f 
for host in nm.all_hosts():     #遍历扫描主机

    print ('-----------------------')
    print('Host: %s (%s)' % (host, nm[host].hostname()))    #输出主机及主机名
    print('State : %s' % nm[host].state())      #输出主机状态

    for proto in nm[host].all_protocols():
        print('---------------------')
        print('protocol : %s'% proto)

        lport = nm[host][proto].keys()  #获取协议所有扫描端口
        #lport.sort()
        lports = sorted(lport)
        for port in lports:  #遍历端口及输出端口状态
            print('port : %s\tstate : %s'%(port, nm[host][proto][port]['state']))

