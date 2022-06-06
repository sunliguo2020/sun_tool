# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/5/30 7:37
"""
import os


def dir_walk(dir_name):
    """
    遍历某个目录，返回其中的所有的文件（包含路径）
    :param dir_name: 要遍历的目录
    :return:
    """
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


def remove_file(file_path):
    if not os.path.isfile(file_path):
        print(f"{file_path} is not a files")
        return -1
    else:
        os.remove(file_path)
        if not os.path.isfile(file_path):
            print(f"{file_path}删除成功")
        else:
            print(f"{file_path}删除失败")
