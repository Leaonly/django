import pexpect
import sys

ip='192.168.129.135'
user='root'
passwd='123456'
target_file='/data/*.yaml'

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip],encoding='utf-8')
fout = open('mylog.txt','w')
child.logifle = sys.stdout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -zcPf /data/yaml.tar.gz ' +target_file)
    child.expect('#')
    print(child.before)
    child.sendline('exit')
    fout.close()
except EOFError:
    print('expect EOF')
except TimeoutError:
    print('expect timeout')

child = pexpect.spawn('/usr/bin/scp', [user+'@'+ip+':/data/yaml.tar.gz','/home'],encoding='utf-8')
fout = open('mylog.txt','a')
child.logfile = sys.stdout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except EOFError:
    print('expect EOF')
except TimeoutError:
    print('expect timeout')

