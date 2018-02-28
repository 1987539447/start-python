#!/usr/bin/env python3
# FileName:use_slots.py
# -*- coding: utf-8 -*-
""" 通过slots限定可动态设置的属性 """


class Student(object):

    @property
    def score(self):
        print('invoke getter')
        return self._score

    @score.setter
    def score(self, value):
        print('invoke setter')
        if not isinstance(value, int):
            raise ValueError('value must be int')
        if value < 0 or value > 100:
            raise ValueError('value must between 0~100')
        self._score = value


s = Student()
s.score = 60
print('s.score = ', s.score)

# ValueError
# s.score = 999


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
