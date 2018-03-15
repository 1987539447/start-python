#!/usr/bin/env python3
# FileName:do_stringio.py
# -*- coding: utf-8 -*-
""" stringio操作。与文件对象一致"""
from io import StringIO


f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')

print(f.getvalue())


f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())




