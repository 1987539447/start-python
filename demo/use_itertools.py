#!/usr/bin/env python3
# FileName:use_itertools.py
# -*- coding: utf-8 -*-
"""  使用itertools 迭代工具 """

import itertools

natuals = itertools.count()
for n in natuals:
    print(n)
    if n >= 50:
        break

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t -= 1
    if t == 0:
        break

ns = itertools.repeat('A', 5)
for c in ns:
    print(c)


natuals = itertools.count()
ns = itertools.takewhile(lambda n: n <= 10, natuals)
for n in ns:
    print(n)

for c in itertools.chain('ABC', 'XYZ'):
    print(c)


for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key,'--', list(group))


# 计算圆周率
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda n: n <= 2*N-1, natuals)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    ns = map(lambda x: 4/x if x % 4 == 1 else -4/x, ns)
    # step 4: 求和:
    return sum(ns)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')