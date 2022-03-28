import pexpect
import sys
#pexpect.Expecter.
child = pexpect.spawn('ssh root@192.168.129.140')
fout = open('mylog.txt',mode='wb')
child.logfile = fout
#child.logfile = sys.stdout

child.expect("(yes/no)?")
child.sendline("yes")
child.expect("password:")
child.sendline("123456")
child.expect('#')
child.sendline('/bin/ls /usr/local/src/')
child.expect("#")