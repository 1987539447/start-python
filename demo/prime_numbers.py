#!/usr/bin/env python3
# FileName:prime_numbers.py
# -*- coding: utf-8 -*-
"""高阶函数filter使用。 素数生成器"""


def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


# 定义从3开始的奇数序列生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义每一轮用于过滤的函数 返回值为过滤函数
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter();
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    main()
