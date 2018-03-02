#!/usr/bin/env python3
# FileName:special_call.py
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self):
        self.name = 'Michel'

    def __call__(self):
        print('My name is %s' % self.name)


s = Student()
s()
