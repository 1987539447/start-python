#!/usr/bin/env python3
# FileName:use_metaclass.py
# -*- coding: utf-8 -*-
""" 通过元类定制类的创建 """


class ListMetaClass(type):
    def __new__(cls, name, base, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, base, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)

