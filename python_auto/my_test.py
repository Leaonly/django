import psutil

# m = psutil.virtual_memory()
# print(m)

# pid_num = 19933
# pid_info = psutil.Process(pid_num)
# print(pid_info.name())
import time 
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

localtime2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(localtime2)

