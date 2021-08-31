import psutil

# m = psutil.virtual_memory()
# print(m)

pid_num = 19933
pid_info = psutil.Process(pid_num)
print(pid_info.name())