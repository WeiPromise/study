#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/20 21:46

import time,multiprocessing,os


def produce(x):
    for i in range(100):
        time.sleep(0.1)
        print('生产了面包:{}->{}'.format(os.getpid(),i))
        x.put('{}'.format(i))

def consumer(x):
   while True:
        time.sleep(0.2)
        print('买了面包:{}->{}'.format(os.getpid(),x.get()))


if __name__ == '__main__':
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=produce,args=(q,))
    p2 = multiprocessing.Process(target=produce,args=(q,))
    p3 = multiprocessing.Process(target=produce,args=(q,))
    c = multiprocessing.Process(target=consumer,args=(q,))
    c1 = multiprocessing.Process(target=consumer,args=(q,))
    c2 = multiprocessing.Process(target=consumer,args=(q,))


    p.start()
    p2.start()
    p3.start()
    c.start()
    c1.start()
    c2.start()