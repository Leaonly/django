# -*- coding: utf-8 -*-

import pexpect
import sys


child = pexpect.spawn('ssh root@192.168.170.153')
# fout = open('mylog.txt','w')
# child.logfile = fout
mypassword = 'wpx2020'
child.expect('password:')
child.sendline(mypassword)
child.expect('#')
child.sendline('touch /tmp/pextest')
child.expect('#')
