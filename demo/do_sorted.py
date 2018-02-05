#!/usr/bin/env python3
# FileName:prime_numbers.py
# -*- coding: utf-8 -*-
"""高阶函数sorted使用。"""
from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))


