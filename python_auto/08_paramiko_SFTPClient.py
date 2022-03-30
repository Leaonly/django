import paramiko

t = paramiko.Transport(('192.168.129.135', 22))
t.connect(username='root', password='123456')
sftp = paramiko.SFTPClient.from_transport(t)

#  put方法 上传本地文件到远程SFTP服务端
localpath = '/data/pv-demo.yaml1'
remotepath = '/tmp/pv-demo.yaml'
# sftp.put(localpath, remotepath)

# get方法 从远程SFTP服务端下载文件到本地。
sftp.get(remotepath, localpath)

'''
SFTPClient类其它常用方法说明：
mkdir,在SFTP服务端创建目录，如sftp.mkdir("/home/userdir",mode=0777),默认模式是0777(八进制)，在某些系统上，mode被忽略。在使用它的地方，当前的umask值首先被屏蔽掉。
remove,删除SFTP服务端指定目录，如sftp.remove("/home/userdir")。
rename,重命名SFTP服务端文件或目录，如sftp.rename("/home/test.sh","/home/testfile.sh")
stat,获取远程SFTP服务端指定文件信息，如sftp.stat("/home/testfile.sh")。
listdir,获取远程SFTP服务端指定目录列表，以Python的列表(List)形式返回，如sftp.listdir("/home")。
'''


