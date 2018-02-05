#!/usr/bin/env python3
# FileName:do_partial.py
# -*- coding: utf-8 -*-
""" 偏函数
固定函数的部分参数：可变参数，关键字参数 从而创建一个新函数
"""
import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

max2 = functools.partial(max, 10)

print('max2(1,2,3) = ', max2(1, 2, 3))
