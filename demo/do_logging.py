#!/usr/bin/env python3
# FileName:do_logging.py
# -*- coding: utf-8 -*-
""" 使用日志"""
import logging


logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10/n)



