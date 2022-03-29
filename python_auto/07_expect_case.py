import pexpect
import sys
from pexpect import *

'''
#pexpect.Expecter.
child = pexpect.spawn('ssh root@192.168.129.135')
fout = open('mylog.txt',mode='wb')
child.logfile = fout
#child.logfile = sys.stdout


child.expect("(yes/no)?")
child.sendline("yes")
child.expect("password:")
child.sendline("123456")
# before成员保存了最近匹配成功之前的内容，affer成员保存了最近匹配成功之后的内容
print("before:"+str(child.before))
print("after:"+str(child.after))
# child.expect('#')
# child.sendline('pwd;/bin/ls /usr/local/src/; echo hello')
# child.expect("#")
child.close()

# run函数应用
mypassword='123456'
fout = open('run.txt',mode='wb')
run('scp mylog.txt root@192.168.129.140:.', events={'(?i)password': mypassword + '\n'}, logfile=fout)
'''

child = pexpect.spawn('ssh root@192.168.129.140', encoding='utf-8')
#fout = open("info.log",'wb')
child.logfile = sys.stdout
child.expect("password:")
child.sendline("123456")
child.expect("#")
child.sendline("echo hello world")
child.expect("#")
child.sendline("exit")
child.expect(pexpect.EOF) 
child.close() 


