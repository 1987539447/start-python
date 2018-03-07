#!/usr/bin/env python3
# FileName:mydict_test.py
# -*- coding: utf-8 -*-
""" Dict类单元测试
    通过增加__name__ 变为可执行脚本 仅把test开头的看作测试例子
"""
import unittest
from mydict import Dict


class TestDict(unittest.TestCase):

    def other_fn(self):
        print('not test case')

    def setUp(self):
        print('---invoke setUp---')

    def tearDown(self):
        print('---invoke tearDown---')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual(d['key'], 'value')
        self.assertTrue('key' in d)

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_keyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
            d['empty']

    def test_attrError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            d.empty


if __name__ == '__main__':
    unittest.main()


