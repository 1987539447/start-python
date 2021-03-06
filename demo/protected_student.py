#!/usr/bin/env python3
# FileName:protected.py
# -*- coding: utf-8 -*-
""" Student Class 私有访问域"""


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


bart = Student('Bart Simpson', 59)

print('bart.get_name() = ', bart.get_name())
bart.set_score(60)
print('bart.get_score() = ', bart.get_score())
bart.print_score()

# print('DO NOT USE bart._Student.__name:', bart._Student.__name)

