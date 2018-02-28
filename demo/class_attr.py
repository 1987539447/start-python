#!/usr/bin/env python3
# FileName:student.py
# -*- coding: utf-8 -*-
""" Student Class 定义使用"""


class Student(object):
    count = 0
    name = 'Student'

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart', 99)
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart', 87)
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


# do not use the same attr
print(Student.name)
bart = Student('Bart', 80)
print(bart.name)
del bart.name
print(bart.name)
