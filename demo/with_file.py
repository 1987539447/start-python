#!/usr/bin/env python3
# FileName:with_file.py
# -*- coding: utf-8 -*-
""" 文件IO操作。"""
from datetime import datetime


with open('test.txt', 'w') as f:
    f.write('今天是：')
    f.write(datetime.now().strftime('%Y-%m-%d'))


with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read....')
    print(s)


with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)




