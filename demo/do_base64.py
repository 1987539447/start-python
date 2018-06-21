#!/usr/bin/env python3
# FileName:do_base64.py
# -*- coding: utf-8 -*-
"""
    测试使用Base64编码
"""

import base64


s = base64.b64encode('在Python中使用Base64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)


s = base64.urlsafe_b64encode('在Python中使用Base64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)


# 请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    if isinstance(s, str):
        s += (4 - len(s) % 4) * '='
    else:
        s += (4 - len(s) % 4) * b'='
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')