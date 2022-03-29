from encodings import utf_8
from sys import stdout 
from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh(encoding='utf-8', logfile=stdout)

    #hostname = input('hostname: ')
    #username = input('username: ')
    password = getpass.getpass('password: ')
    s.login('192.168.129.140', 'root' ,password)
    s.sendline('uptime')
    s.prompt()
    #print(s.before)
    s.sendline('ls /data')
    s.prompt()
    #print(s.before)

    s.logout()
except pxssh.ExceptionPxssh as e:
    print('pxssh failed on login.')
    print(e)
