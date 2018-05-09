#!/usr/bin/env python3
# FileName:pooled_processing.py
# -*- coding: utf-8 -*-
""" 进程池 实现多进程"""


from multiprocessing import Pool
import os, random, time


# 子进程运行的代码
def long_time_task(name):
    print('Run task %s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random * 20)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end-start)))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('wait for all process done...')
    p.close()
    p.join()
    print('All process done')

