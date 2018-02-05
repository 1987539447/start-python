#!/usr/bin/env python3
# FileName:return_func.py
# -*- coding: utf-8 -*-
""" 返回函数 """


def lazy_sum(*args):
    def sum_numbers():
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum_numbers


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())


# f1() f2() f3() returns 9,9,9 rather than 1,4,9
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# fix
def count():
    fs = []

    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 引用的外部变量不能被修改
def create_counter():
    f = [0]

    def counter():
        f[0] += 1
        return f[0]
    return counter


# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
