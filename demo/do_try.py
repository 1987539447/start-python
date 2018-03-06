#!/usr/bin/env python3
# FileName:do_try.py
# -*- coding: utf-8 -*-
""" try except raise finally 错误处理。"""


try:
    print('try...')
    r = 10 / 0
    print('result :',r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')

print('END')


