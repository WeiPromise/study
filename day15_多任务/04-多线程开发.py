#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/19 22:54

import time,threading


# 多线程可以同时操作一个全局变量（多个线程共享全局变量）
# 线程安全问题
ticket = 100

lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:

        time.sleep(2)
        print('{}在睡觉'.format(threading.current_thread().name))
        lock.acquire()
        if ticket > 0:
            time.sleep(0.5)
            ticket -= 1
            lock.release()
            print('{}:卖出去一张票，还剩{}'.format(threading.current_thread().name,ticket))
        else:
            lock.release()
            print('票卖完了')
            break


t1 = threading.Thread(target=sell_ticket)
t2 = threading.Thread(target=sell_ticket)
t3 = threading.Thread(target=sell_ticket)
t4 = threading.Thread(target=sell_ticket)
t5 = threading.Thread(target=sell_ticket)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()