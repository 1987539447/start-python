#!/usr/bin/env python3
# FileName:err.py
# -*- coding: utf-8 -*-
""" 错误的异常栈"""


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()


