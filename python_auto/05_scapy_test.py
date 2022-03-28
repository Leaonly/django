import os,sys,time,subprocess
import warnings,logging

warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import traceroute
domains = input('pls input one or more IP/domain: ')
target = domains.split(' ')
dport = [80]

if len(target) >= 1 and target[0] !='':
    res,unans = traceroute(target,dport=dport,retry=-2)
    #res.graph(target="> test.svg")
    time.sleep(1)
    #subprocess.Popen('')
else:
    print('IP/domain num of errors.exit')
