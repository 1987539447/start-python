#!/usr/bin/env python3
# FileName:do_mixin.py
# -*- coding: utf-8 -*-
""" 多重继承 mixin
多重继承用C3算法解析方法顺序
http://www.codeweblog.com/python-mro-c3%E7%AE%97%E6%B3%95/
拓扑排序
https://kevinguo.me/2018/01/19/python-topological-sorting/
"""


class A(object):

    def foo(self):
        print('A foo')

    def bar(self):
        print('A bar')


class B(object):

    def foo(self):
        print('B foo')

    def bar(self):
        print('B bar')


class C1(A):
    pass


class C2(B):
    def bar(self):
        print('C2-bar')


class D(C1, C2):

    pass


if __name__ == '__main__':
    print(D.__mro__)
    d = D()
    d.foo()
    d.bar()




