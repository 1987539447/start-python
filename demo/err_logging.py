#!/usr/bin/env python3
# FileName:err_logging.py
# -*- coding: utf-8 -*-
""" 通过日志记录异常信息"""
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')


