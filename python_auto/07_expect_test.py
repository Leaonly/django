import pexpect, sys

child = pexpect.spawn('ssh', ['root@192.168.129.140'])
child.expect

shell_cmd = 'ls -l | grep LOG > logs.txt'
child = pexpect.spawn('/bin/bash', ['-c', shell_cmd])
child.expect(pexpect.EOF)

# 调试信息 一种为写到日志文件，另一种为输出到标准输出
# In Python 2:
child = pexpect.spawn('some_command')
child.logfile = sys.stdout

# In Python 3, we'll use the ``encoding`` argument to decode data
# from the subprocess and handle it as unicode:
child = pexpect.spawn('some_command', encoding='utf-8')
child.logfile = sys.stdout

child = pexpect.spawn('some_command')
child.close()
print(child.exitstatus, child.signalstatus)
