#!/usr/bin/env python3
# FileName:use_slots.py
# -*- coding: utf-8 -*-
""" 通过slots限定可动态设置的属性 """


class Student(object):

    __slots__ = ('name', 'age')


class GraduateStudent(Student):
    pass


class AnotherStudent(Student):
    __slots__ = ('score')


s = Student()
s.name = 'Michale'
s.age = 25

# Error:AttributeError

try:
    s.score = 90
except AttributeError as e:
    print('AttributeError', e)

# with no __slots__
g = GraduateStudent()
g.score = 99
print('g.score=', g.score)

another = AnotherStudent()
another.name = 'Jack'
another.score = 99
print('another.name=', another.name)
print('another.score=', another.score)


