#!/usr/bin/env python3
# FileName:use_pickle.py
# -*- coding: utf-8 -*-
""" 通过pickle序列化对象"""
import pickle


bob = dict(name='Bob', age=20, score=88)
data = pickle.dumps(bob)
print(data)

re_bob = pickle.loads(data)
print(re_bob)






