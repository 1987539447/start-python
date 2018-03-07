#!/usr/bin/env python3
# FileName:do_pdb.py
# -*- coding: utf-8 -*-
""" 使用pdb调试"""
import pdb

s = '0'
n = int(s)
# 运行到这里会自动暂停
pdb.set_trace()
print(10 / n)



