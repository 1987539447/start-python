#!/usr/bin/env python3
# FileName:do_dir.py
# -*- coding: utf-8 -*-
""" 实现 dir -l 命令"""
from datetime import datetime
import os


pwd = os.path.abspath('.')

print('        Size          Last Modified            Name')
print('---------------------------------------------------------------------')

for x in os.listdir(pwd):
    size = os.path.getsize(x)
    mtime = datetime.fromtimestamp(os.path.getmtime(x)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(x) else ''
    print('%10d     %s       %s%s ' % (size, mtime, x, flag))


def find_file(p, target):

    for root, dirs, files in os.walk(os.path.abspath(p), topdown=False):
        for x in files:
            if target in x:
                print(x, '---->', root)


target = str(input('输入文件名...:'))
p = str(input('输入目录...:'))
find_file(p,target)





