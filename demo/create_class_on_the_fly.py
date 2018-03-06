#!/usr/bin/env python3
# FileName:create_class_on_the_fly.py
# -*- coding: utf-8 -*-
""" 通过type动态创建类 """


def fn(self, name='world'):
    print('Hello %s' % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print('call hello():')
h.hello()

print('type(Hello)=', type(Hello))
print('type(h)=', type(h))
