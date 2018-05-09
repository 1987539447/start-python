#!/usr/bin/env python3
# FileName:do_fork.py
# -*- coding: utf-8 -*-
""" fork 进程 仅Unix平台"""


import os

print('Process (%s) starting.....' % os.getpid())

# only unix or linux
pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is (%s)' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process (%s)' % (os.getpid(), pid))

