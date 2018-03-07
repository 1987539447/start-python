#!/usr/bin/env python3
# FileName:do_assert.py
# -*- coding: utf-8 -*-
""" 使用断言 抛出AssertionError"""


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


def main():
    foo('0')


main()


