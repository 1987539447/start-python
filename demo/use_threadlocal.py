#!/usr/bin/env python3
# FileName:use_threadlocal.py
# -*- coding: utf-8 -*-
""" 通过threadlocal在线程内共享数据"""


import threading

local_school = threading.local()


def process_student():
    stu = local_school.student
    print('Hello %s in (%s)' % (stu, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thrad-B')

t1.start()
t2.start()
t1.join()
t2.join()

