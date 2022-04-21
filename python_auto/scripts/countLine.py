# coding=utf-8

import os 
import time 
# 设定目录
basedir = '/data'
filelists = []
# 指定想要统计的文件类型
whitelist = ['cpp','sh']
# 遍历文件
def getFile(basedir):
    global filelists
    for parent,dirnames,filenames in os.walk(basedir):
        for filename in filenames:
            ext = filename.split('.')[-1]
            #只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent,filename))
                
# 统计一个行数
def countLine(fname):
    count = 0
    # 把文件做二进制看待，read
    for file_line in open(fname,'rb').readlines():
        if file_line != '' and file_line != '\n': #过滤空行
            count += 1
    print (fname + ' ----', count)
    return count
                
if __name__ == '__main__':
    startTime = time.clock()
    getFile(basedir)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print('total lines:', totalline)
    print ('Done! Cost Time: %0.2f second' % (time.clock() - startTime))
