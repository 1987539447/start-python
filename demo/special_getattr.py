#!/usr/bin/env python3
# FileName:special_getattr.py
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self):
        self.name = 'Michel'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda year: year - 1987
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print(s.name)
print(s.score)
print(s.age(2018))
#Attribute error
print(s.grade)
