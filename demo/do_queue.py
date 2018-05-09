#!/usr/bin/env python3
# FileName:do_queue.py
# -*- coding: utf-8 -*-
""" 通过队列queue进行进程间通信"""


from multiprocessing import Process,Queue
import os, time, random


# 向队列写数据
def write(q):
    print('Process to write %s' % os.getpid())
    for x in ['A', 'B', 'C', 'D']:
        print('put %s to queue....' % x)
        q.put(x)
        time.sleep(random.random() * 20)


# 从队列读数据
def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        r = q.get(True)
        print('Get %s from queue' % r)


if __name__ == '__main__':
    q = Queue()
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    # 启动读写进程
    pw.start()
    pr.start()
    # 等待写进程结束
    pw.join()
    # 读进程强制结束
    pr.terminate()


