#!/usr/bin/env python3
# FileName:use_json.py
# -*- coding: utf-8 -*-
""" 使用json 转化对象 dict"""
import json


bob = dict(name='Bob', age=20, score=88)
json_str = json.dumps(bob)
print('json str--', json_str)
reborn = json.loads(json_str)
print(reborn)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s %s %s)' % (self.name, self.age, self.score)


s = Student('Michel', 21, 99)
stu_data = json.dumps(s, default=lambda obj:obj.__dict__)
print('to json--', stu_data)
rebuild = json.loads(stu_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

