#!/usr/bin/env python3
# FileName:get_type.py
# -*- coding: utf-8 -*-
""" type()使用 来获取对象类型 """
import types

# type()
print('type(123)= ', type(123))
print('type(\'123\')=', type('123'))
print('type(None)=', type(None))
print('type(abs)=', type(abs))


# types
print('type(\'abc\')==str', type('abc') == str)

print('type(abs)==types.BuiltinFunctionType',
      type(abs) == types.BuiltinFunctionType)
