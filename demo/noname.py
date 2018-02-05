#!/usr/bin/env python3
# FileName:return_func.py
# -*- coding: utf-8 -*-
""" 匿名函数 """


print("匿名函数")


# 将匿名函数作为返回值
def build(x,y):
    return lambda: x*x+y*y


q = build(5, 8)
print(q())
