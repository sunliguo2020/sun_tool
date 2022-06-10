#!/usr/bin/python
"""
统计当前文件夹下面，各个文件夹下文件的个数（只统计第一层）
2022-02-21:修改为python3版本
"""

import os

Total = 0

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

fileList = os.listdir('./')

for i in fileList:
    if os.path.isdir(i):
        # dir_len = len(os.listdir(i))
        count = 0
        for root, dirs, files in os.walk(i):
            fileLength = len(files)
            if fileLength != 0:
                count = count + fileLength
        print("%s:\t%r" % (i, count))

        Total = Total + count

print("Total:\t%r" % Total)
