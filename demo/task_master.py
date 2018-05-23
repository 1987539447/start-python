#!/usr/bin/env python3
# FileName:task_master.py
# -*- coding: utf-8 -*-
""" 分布式进程 master进程"""


import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue;


if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    manager = QueueManager(address=('', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %s' % n)
        task.put(n)

    print('Try get result....')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result %s' % r)

    manager.shutdown()
    print('master exit')



