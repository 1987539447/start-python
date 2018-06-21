#!/usr/bin/env python3
# FileName:regex.py
# -*- coding: utf-8 -*-
"""
    正则表达式测试
"""

import re


print('Test: 010-12345')
m = re.match(r'(\d{3})\-(\d{3,8})', '010-12345')
print(m.group(0), m.group(1), m.group(2))

t = '19:05:30'
print('Test:', t)
m = re.match(r'^([0-9]|0[0-9]|1[0-9]|[2][0-3])\:([0-5][0-9]|[0-9])\:([0-5][0-9])$', t)
print(m.groups())


def is_valid_email(addr):
    regex = r'^[a-z.]+?\@[a-z]+?\.com$'
    if re.match(regex, addr):
        return True
    return False


def name_of_email(addr):
    if re.match(r'<', addr):
        regex = r'^<([a-zA-Z\s]+)>\s([a-z]+?)@(\w+?.\w{3})$'
    else:
        regex = r'^([a-z]+?)@(\w+?.\w{3})$'
    m = re.match(regex, addr)
    # print(m.groups())
    return m.group(1)


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.com') == 'tom'
print('ok')
