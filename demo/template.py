#!/usr/bin/env python3
# FileName:do_generator.py
# -*- coding: utf-8 -*-
"""模块说明.

模块描述
多行
多行.

举例:
    举例说明::

        $ python example_google.py

其它说明,结尾引号单独一行.
"""

__author__ = ''
import sys


class A:

    def __init__(self):
        pass

    def hello(self):
        pass


def main():
    pass


def func(arg1, arg2):
    """在这里写函数的一句话总结(如: 计算平均值).

    这里是具体描述.

    参数
    ----------
    arg1 : int
        arg1的具体描述
    arg2 : int
        arg2的具体描述

    返回值
    -------
    int
        返回值的具体描述

    参看
    --------
    otherFunction : 其它关联函数等...

    示例
    --------
    示例使用doctest格式, 在`>>>`后的代码可以被文档测试工具作为测试用例自动运行

    >>> a=[1,2,3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    """


print(sys.path)

