import sys
import nmap

scan_row=[]
input_data=input('pls input hosts and port: ')
scan_row = input_data.split(' ')
if len(scan_row)!=2:
    print('input errors, example \"192.168.1.0/24 80,443\"')
    sys.exit(0)
hosts=scan_row[0]
port=scan_row[1]

try: 
    nm = nmap.PortScanner()
except Exception as e:#nmap.PortScannerError:
    print('nmap not found', sys.exc_info()[0], str(e))
    sys.exit(0)
except:
    print('unexcepted error:', sys,sys.exc_info()[0])
    sys.exit(0)

try:
    # 调用扫描方法
    nm.scan(hosts=hosts, arguments=' -v -sS -p '+port)
except Exception as e:
    print('scan error:'+str(e))

for host in nm.all_hosts():
    print('---------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname())) # 输出主机名
    print('State : %s'% nm[host].state())

    for proto in nm[host].all_protocols():
        print('-------------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        lport.sort()
        for prot in lport :
            print ('port : %s\tstate: %s'%(port, nm[host][proto][port]['state']))

# 10.0.69.129 80