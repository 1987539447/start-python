#!/usr/bin/env python3
# FileName:use_collections.py
# -*- coding: utf-8 -*-
"""
    测试使用集合类
"""

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] = ', dd['key1'])
print('dd[\'key2\'] = ', dd['key2'])

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
