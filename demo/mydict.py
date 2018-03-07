#!/usr/bin/env python3
# FileName:mydict.py
# -*- coding: utf-8 -*-
""" 自定义Dict实现 支持按属性取值"""


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value


