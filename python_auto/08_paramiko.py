from base64 import decode
import paramiko

hostname = '192.168.129.135'
username = 'root'
password = '123456'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.load_system_host_keys()     #获取客户端host_keys,默认~/.ssh/known_hosts,非默认路径需指定
ssh.connect(hostname=hostname, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('free -h')
print(stdout.read().decode('utf_8'))
ssh.close()