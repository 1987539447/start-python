#!/usr/bin/env python3
# FileName:use_datetime.py
# -*- coding: utf-8 -*-
"""
    datetime使用测试
"""

from datetime import datetime, timedelta, timezone
import re

# 获取当前时间
now = datetime.now()
print('now=', now)
print('type(now)', type(now))


# 用指定日期创建datetime
dt = datetime(2018, 6, 19)
print('dt=', dt)


# 把datetime转为timestamp
print('datetime-->timestamp', dt.timestamp())

# 把timestamp转为datetime
t = dt.timestamp()
print('timestamp-->datetime', datetime.fromtimestamp(t))
print('timestamp--> datetime as UTC-0', datetime.utcfromtimestamp(t))

# 从str读取时间
cday = datetime.strptime('2018-6-19 20:31:00', '%Y-%m-%d %H:%M:%S')
print('strptime', cday)

# 把datetime格式化输出
print('strftime', cday.strftime('%a, %b %d %H:%M'))

# 日期进行加减
cday = datetime.now()
print('current datetime', cday)
print('current + 10 houres', cday + timedelta(hours=10))
print('current - 1 day', cday - timedelta(days=1))
print('current + 2.5 days', cday + timedelta(days=1, hours=12))

# 把时间从UTC0转为UTC8
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('utc+0:00 now', utc_dt)
print('utc+8:00 now', utc8_dt)

# 测试带时区时间转换
def to_timestamp(dt_str, tz_str):
    re_utc = re.compile(r'(UTC)([+|-][0-9]+:00)')
    if re.match(re_utc, tz_str):
        h = re.match(re_utc, tz_str).group(2).split(':')[0]
        print(re.match(re_utc, tz_str).group(2).split(':'))
        hour = int(h)
    else:
        raise ValueError("Data unavailable")
    cdate = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    nowDate = cdate.replace(tzinfo=timezone(timedelta(hours=hour)))
    print(nowDate)
    timeStamp = nowDate.timestamp()
    print(timeStamp)
    return timeStamp


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')