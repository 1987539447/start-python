#!/usr/bin/env python3
# FileName:do_map.py
# -*- coding: utf-8 -*-
"""高阶函数map使用。"""


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def normalize(name):
    return name[0].upper() + name.lower()[1:-1]


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)