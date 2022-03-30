from fabric.api import *

env.user = 'root'
env.hosts = ['localhost']
env.password = '123456'

@runs_once      #查看本地系统信息，当有多台主机时只运行一次
def local_task():
    local('uname -a')

def remote_task():
    with cd('/root'):    #"with"的作用是让后面的表达式的语句继承当前状态，实现"cd /root/ && ls -l'的效果
        run('ls -l')
        
@runs_once      #主机遍历过程中，只有第一台触发此函数
def input_raw():
    return prompt("pls input dir name: ",default="/home")

def worktask(dirname):
    run("ls -l "+dirname)

@task       #限定只有go函数对fab命令可见
def go():
    getdirname = input_raw()
    worktask(getdirname)


