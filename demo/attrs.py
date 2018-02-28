#!/usr/bin/env python3
# FileName:attrs.py
# -*- coding: utf-8 -*-
""" 操作对象属性-方法"""


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print('has attribute x?', hasattr(obj, 'x'))
print('has attribute y?', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('has attribute y?', hasattr(obj, 'y'))
print('getattr(obj, \'y\')=', getattr(obj, 'y'))
print('obj.y=', obj.y)

f = getattr(obj, 'power')
print(f)
print(f())
