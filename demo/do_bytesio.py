#!/usr/bin/env python3
# FileName:do_bytesio.py
# -*- coding: utf-8 -*-
"""  bytesio操作。二进制读写"""
from io import BytesIO


f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world')

print(f.getvalue())

data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('UTF-8')
f = BytesIO(data)
print(f.read())


