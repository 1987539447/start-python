#!/usr/bin/env python3
# FileName:decorator.py
# -*- coding: utf-8 -*-
""" 装饰器函数 """
import functools
import time


def log(func):
    def wrapper(*args, **kw):
        print('call %s() ' % func.__name__)
        func(*args, **kw)
    return wrapper


@log
def now():
    print('2018')


now()
print(now.__name__)


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s' % (text, func.__name__))
            func(*args, **kw)
        return wrapper
    return decorator


@logger('execute')
def today():
    print('2018-02-02')


today()
print(today.__name__)


def metric(fn):
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - start))
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')