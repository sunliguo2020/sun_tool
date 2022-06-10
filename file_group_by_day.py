#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 2020-04-19
@author: sunliguo
2022-02-14:增加多进程（多线程）
2022-02-17:线程池
2022-02-10:file_list yield 生产要分析文件的列表
2022-02-20:绝对路径转相对路径

"""
import os
import threading
import time
from threading import Thread


def mymove_file(src, dst):
    """
    移动文件
    @param src: 源文件
    @param dst: 目标文件
    @return:
    """

    if not os.path.isfile(src):
        print('%s not exist!' % (src))
        return -1
    else:
        fpath, fname = os.path.split(dst)
        # print(fpath)

    # 判断目标文件夹是否存在
    if not os.path.isdir(fpath):
        os.makedirs(fpath)
    # 判断目标文件是否已经存在
    if os.path.isfile(dst):
        print('目标文件：%s 已经存在!' % dst)
    else:
        try:
            os.rename(src, dst)
            print('move {0}->{1}'.format(src, dst))
        except Exception as e:
            print(e)


def path_add_day(file_list):
    """
    按照文件的创建日期，路径前添加创建日期
    @param file_list:
    @return:
    """

    for each_file in file_list:
        print("当前threading name为:", threading.current_thread().name)
        print(each_file)
        file_dir, file_name = os.path.split(each_file)
        # 文件的创建时间,有可能别的程序移动了。
        try:
            file_mtime = os.stat(each_file).st_mtime
            file_modify_time = time.strftime('%Y-%m-%d', time.localtime(file_mtime))
        except Exception as e:
            print(e)
            return -1
        # 给路径添加 文件创建的时间。
        dstfile = os.path.join(file_dir, file_modify_time, file_name)

        mymove_file(each_file, dstfile)


def list_of_groups(init_list, n):
    """
    将原列表分割，组成列表后返回。
    @param init_list: 原列表
    @param n: 分割列表的个数
    @return:
    """
    return [init_list[i:i + n] for i in range(0, len(init_list), n)]


def file_list(base_dir=os.getcwd()):
    """
    返回要分析的文件列表
    @param base_dir:
    @return:
    """
    # 所有要分析的文件列表（包含路径）
    reldir = os.path.relpath(base_dir)
    # print('base_dir=', base_dir)
    # 列出要分析的文件，yield 返回
    for file in os.listdir(reldir):
        file_full_path = os.path.join(reldir, file)

        if os.path.isfile(file_full_path) and (file_full_path.endswith('.txt')):
            yield file_full_path


if __name__ == '__main__':
    # 线程池
    # pool = Pool(4)
    # pool.map(path_add_day, (file_list(os.getcwd()),))
    # pool.close()

    # 多进程
    """p1 = multiprocessing.Process(target=path_add_day, args=(file_list,))
    p1.start()"""

    # 多线程
    ts = []
    count = 0
    for i in file_list(os.getcwd()):
        print("count = ", count)
        # print(i)
        file_l = []
        file_l.append(i)
        t = Thread(target=path_add_day, args=(file_l,), name="thread " + str(count))
        ts.append(t)
        t.start()

        print("当前活动的进程数为：",threading.active_count())

        count = count + 1
    for j in ts:
        j.join()
